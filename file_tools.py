import os
import csv
import hashlib
import zipfile
import json
from datetime import datetime
from typing import List, Union, Tuple, Dict, Any, Optional

# ==========================================
# 1. Directory & Path Operations
# ==========================================

def get_cwd() -> str:
    """Returns the Current Working Directory (CWD)."""
    return os.getcwd()

def change_dir(path: str) -> None:
    """Changes the current working directory to the specified path."""
    os.chdir(path)

def list_dir_items(path: str) -> List[str]:
    """Lists all files and directories in the specified path."""
    return os.listdir(path=path)

def path_exists(path: str) -> bool:
    """Checks if a path exists (file or directory)."""
    return os.path.exists(path)

def is_file(path: str) -> bool:
    """Checks if the path is a regular file."""
    return os.path.isfile(path)

def is_dir(path: str) -> bool:
    """Checks if the path is a directory."""
    return os.path.isdir(path)

def is_link(path: str) -> bool:
    """Checks if the path is a symbolic link."""
    return os.path.islink(path)

def normalize_path(path: str) -> str:
    """Normalizes the path (removes redundant separators, resolves '.' and '..')."""
    return os.path.normpath(path)

def get_abspath(path: str) -> str:
    """Converts a relative path to an absolute path."""
    return os.path.abspath(path)

def get_basename(path: str) -> str:
    """Extracts the filename (with extension) from a path."""
    return os.path.basename(path)

def get_dirname(path: str) -> str:
    """Extracts the directory portion of a path."""
    return os.path.dirname(path)

def join_paths(*args: str) -> str:
    """Joins one or more path components intelligently."""
    return os.path.join(*args)

def split_path(path: str) -> Tuple[str, str]:
    """Splits path into (directory, filename)."""
    return os.path.split(path)

def split_extension(path: str) -> Tuple[str, str]:
    """Splits path into (root_name, extension)."""
    return os.path.splitext(path)

def get_script_dir() -> str:
    """Returns the absolute directory of the current Python script."""
    return os.path.dirname(os.path.abspath(__file__))

# ==========================================
# 2. File Read/Write Operations
# ==========================================

def read_file(path: str) -> str:
    """Reads file content with UTF-8 encoding."""
    with open(path, "r", encoding="utf-8") as f:
        return f.read()

def write_file(path: str, content: str) -> None:
    """Writes content to a file with UTF-8 encoding (overwrites if exists)."""
    with open(path, "w", encoding="utf-8") as f:
        f.write(content)

def read_csv(path: str) -> List[List[str]]:
    """Reads a CSV file and returns a nested list."""
    with open(path, newline="", encoding="utf-8") as csvfile:
        return list(csv.reader(csvfile))

def write_csv(path: str, data: List[List[Any]]) -> None:
    """Writes a nested list to a CSV file."""
    with open(path, "w", newline="", encoding="utf-8") as csvfile:
        writer = csv.writer(csvfile)
        writer.writerows(data)

def batch_replace(folder_path: str, old_str: str, new_str: str) -> None:
    """Replaces old string with new string in all files within a directory."""
    for filename in os.listdir(folder_path):
        path = os.path.join(folder_path, filename)
        if os.path.isfile(path):
            try:
                content = read_file(path)
                new_content = content.replace(old_str, new_str)
                write_file(path, new_content)
            except Exception as e:
                print(f"Failed to process {path}: {e}")

def get_char_count(path: str) -> int:
    """Returns the character count of a file."""
    return len(read_file(path))

# ==========================================
# 3. System & Process Info
# ==========================================

def make_dir(path: str) -> None:
    """Creates a single-level directory."""
    os.mkdir(path)

def make_dirs(path: str) -> None:
    """Creates recursive multi-level directories."""
    os.makedirs(path, exist_ok=True)

def remove_dir(path: str) -> None:
    """Removes an empty directory."""
    os.rmdir(path)

def remove_dirs(path: str) -> None:
    """Removes empty directories recursively."""
    os.removedirs(path)

def get_file_size(path: str) -> int:
    """Returns file size in bytes."""
    return os.path.getsize(path)

def get_env_var(name: str) -> Optional[str]:
    """Gets the value of an environment variable."""
    return os.getenv(name)

def set_env_var(name: str, value: str) -> str:
    """Sets an environment variable."""
    os.environ[name] = value
    return value

def run_system_cmd(command: str) -> int:
    """Executes a system command in a sub-shell."""
    return os.system(command)

def get_username() -> str:
    """Returns the current logged-in username."""
    return os.getlogin()

def get_cpu_count() -> Optional[int]:
    """Returns the number of CPU cores."""
    return os.cpu_count()

def rename_item(old_name: str, new_name: str) -> None:
    """Renames a file or directory."""
    os.rename(old_name, new_name)

def delete_file(path: str) -> None:
    """Deletes a file."""
    os.remove(path)

def get_mtime(path: str) -> float:
    """Returns last modification time (timestamp)."""
    return os.path.getmtime(path)

def get_ctime(path: str) -> float:
    """Returns creation time (timestamp)."""
    return os.path.getctime(path)

def create_symlink(source: str, link_name: str) -> None:
    """Creates a symbolic link."""
    os.symlink(source, link_name)

def change_permission(path: str, mode: int) -> None:
    """Changes file permissions (e.g., mode=0o755)."""
    os.chmod(path, mode)

def get_pid() -> int:
    """Returns current process ID."""
    return os.getpid()

def get_ppid() -> int:
    """Returns parent process ID."""
    return os.getppid()

def walk_dir(path: str) -> Optional[Dict[str, Any]]:
    """Returns the root, dirs, and files for the first level of a directory walk."""
    for root, dirs, files in os.walk(path):
        return {"root": root, "dirs": dirs, "files": files}

def create_zip(zip_name: str, files_to_add: List[str]) -> None:
    """Creates a zip archive from a list of files."""
    with zipfile.ZipFile(file=zip_name, mode="w") as zf:
        for file_path in files_to_add:
            if os.path.exists(file_path):
                zf.write(file_path)

# ==========================================
# 🆕 New Feature: Unified File Info
# ==========================================

def get_file_info(path: str, calculate_hash: bool = False) -> Dict[str, Any]:
    """
    Enhanced file information retrieval.
    
    Args:
        path (str): The path to the file or directory.
        calculate_hash (bool): Whether to compute the SHA256 hash (can be slow for large files).
    """
    if not os.path.exists(path):
        return {"error": "Path does not exist"}
    
    stats = os.stat(path)
    is_file = os.path.isfile(path)
    
    # 1. Human Readable Size Conversion
    def format_size(size_bytes: int) -> str:
        if size_bytes == 0: return "0B"
        units = ("B", "KB", "MB", "GB", "TB")
        import math
        i = int(math.floor(math.log(size_bytes, 1024)))
        p = math.pow(1024, i)
        s = round(size_bytes / p, 2)
        return f"{s} {units[i]}"

    # 2. File Checksum (SHA256)
    file_hash = None
    if is_file and calculate_hash:
        sha256_hash = hashlib.sha256()
        with open(path, "rb") as f:
            for byte_block in iter(lambda: f.read(4096), b""):
                sha256_hash.update(byte_block)
        file_hash = sha256_hash.hexdigest()

    # 3. Line Count (for text files)
    line_count = 0
    if is_file:
        try:
            with open(path, 'rb') as f:
                line_count = sum(1 for _ in f)
        except Exception:
            line_count = None # Not a text file or unreadable

    return {
        "name": os.path.basename(path),
        "abs_path": os.path.abspath(path),
        "type": "file" if is_file else "directory",
        "size_raw": stats.st_size,
        "size_readable": format_size(stats.st_size),
        "last_modified": datetime.fromtimestamp(stats.st_mtime).strftime('%Y-%m-%d %H:%M:%S'),
        "created_time": datetime.fromtimestamp(stats.st_ctime).strftime('%Y-%m-%d %H:%M:%S'),
        "permissions": oct(stats.st_mode & 0o777), # e.g., '0o644'
        "hash_sha256": file_hash,
        "line_count": line_count,
        "extension": os.path.splitext(path)[1].lower()
    }
h = get_file_info("file_tools.py")
print(h)