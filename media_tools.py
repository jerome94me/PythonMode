import os
from typing import Any, Dict, Union, List
import yt_dlp

class YouTubeDownloader:
    """
    A comprehensive utility class for interacting with YouTube content.
    Supports video/audio downloads, metadata retrieval, and keyword searching.
    """

    @staticmethod
    def download_video(url: str, resolution: Union[int, str] = '1080', sub_dir: str = "videos") -> Dict[str, str]:
        """
        Download a YouTube video with a specified maximum resolution.
        
        :param url: The URL of the YouTube video.
        :param resolution: Max height (e.g., 720, 1080) or 'best'.
        :param sub_dir: The subdirectory to save the video.
        :return: A dictionary containing the status and file path.
        """
        if not os.path.exists(sub_dir):
            os.makedirs(sub_dir)

        format_str = "bestvideo+bestaudio/best" if resolution == 'best' else f"bestvideo[height<={resolution}]+bestaudio/best"
        out_tmpl = os.path.join(os.getcwd(), sub_dir, '%(title)s.%(ext)s')
        
        opts = {
            "format": format_str,
            'outtmpl': out_tmpl,
            'merge_output_format': 'mp4',
            'quiet': True,
            'extractor_args': {'youtube': {'player_client': ['android', 'web']}},
        }
        
        try:
            with yt_dlp.YoutubeDL(opts) as ydl:
                ydl.download([url])
                return {
                    "status": "success", 
                    "message": "Video download completed", 
                    "path": out_tmpl
                }
        except Exception as e:
            return {"status": "failed", "message": str(e)}

    @staticmethod
    def download_audio(url: str, sub_dir: str = "music") -> Dict[str, str]:
        """
        Download the audio from a YouTube video and convert it to MP3.
        
        :param url: The URL of the YouTube video.
        :param sub_dir: The subdirectory to save the audio.
        :return: A dictionary containing the status.
        """
        if not os.path.exists(sub_dir):
            os.makedirs(sub_dir)

        out_tmpl = os.path.join(os.getcwd(), sub_dir, '%(title)s.%(ext)s')
        opts = {
            'format': 'bestaudio/best',
            'postprocessors': [{
                'key': 'FFmpegExtractAudio',
                'preferredcodec': 'mp3',
                'preferredquality': '192',
            }],
            'outtmpl': out_tmpl,
            'quiet': True,
        }
        
        try:
            with yt_dlp.YoutubeDL(opts) as ydl:
                ydl.download([url])
                return {"status": "success", "message": "Audio download and conversion completed"}
        except Exception as e:
            return {"status": "failed", "message": str(e)}

    @staticmethod
    def get_info(url: str) -> Dict[str, Any]:
        """
        Fetch video metadata without downloading the file.
        
        :param url: The URL of the YouTube video.
        :return: A dictionary containing title, views, duration, etc.
        """
        opts = {'quiet': True}
        try:
            with yt_dlp.YoutubeDL(opts) as ydl:
                info = ydl.extract_info(url, download=False)
                return {
                    "status": "success",
                    "title": info.get('title'),
                    "views": info.get('view_count'),
                    "likes": info.get('like_count'),
                    "duration_sec": info.get('duration'),
                    "upload_date": info.get('upload_date'),
                    "resolution": f"{info.get('width')}x{info.get('height')}",
                    "channel": info.get('uploader'),
                    "thumbnail": info.get('thumbnail')
                }
        except Exception as e:
            return {"status": "failed", "error": str(e)}

    @staticmethod
    def search_video(keyword: str, count: int = 1) -> Dict[str, Any]:
        """
        Search for videos based on keywords and return information for the first result.
        
        :param keyword: The search term.
        :param count: Number of results to retrieve (default 1).
        :return: A dictionary containing details of the first search result.
        """
        url = f"ytsearch{count}:{keyword}"
        opts = {'quiet': True}
        try:
            with yt_dlp.YoutubeDL(opts) as ydl:
                info = ydl.extract_info(url, download=False)
                if not info.get('entries'):
                    return {"status": "failed", "message": "No results found"}
                    
                first_video = info['entries'][0]
                return {
                    "status": "success",
                    "title": first_video.get('title'),
                    "url": first_video.get('webpage_url'),
                    "views": first_video.get('view_count'),
                    "duration": first_video.get('duration')
                }
        except Exception as e:
            return {"status": "failed", "error": str(e)}

# Example Usage:
# if __name__ == "__main__":
#     downloader = YouTubeDownloader()
#     result = downloader.get_info("https://www.youtube.com/watch?v=example")
#     print(result)