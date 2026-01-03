import json
import file_tools
from typing import TextIO, Dict, List, Union, Optional, Any

# ==========================================
# JSON Processing Utilities
# ==========================================

def load_json(file_stream: TextIO) -> Union[Dict, List]:
    """
    [讀取並轉換] 
    Reads an opened JSON file stream and converts it to a Python dict or list.
    
    Mapping Reference:
        JSON Object -> Python dict
        JSON Array  -> Python list
        JSON String -> Python str
        JSON Number -> Python int/float
        JSON True   -> Python True
        JSON False  -> Python False
        JSON Null   -> Python None
    """
    return json.load(file_stream)

def dump_json(file_stream: TextIO, data: Union[Dict, List], indent: Optional[int] = None) -> None:
    """
    [轉換並寫入]
    Serializes Python data into JSON format and writes it to an opened file stream.
    """
    json.dump(data, file_stream, indent=indent, ensure_ascii=False)

def parse_json_string(json_str: str) -> Union[Dict, List]:
    """
    [字串轉物件]
    Converts a JSON formatted string into a Python dictionary or list.
    """
    return json.loads(json_str)

def to_json_string(data: Union[Dict, List], indent: Optional[int] = None) -> str:
    """
    [物件轉字串]
    Converts a Python object into a JSON formatted string.
    """
    return json.dumps(data, indent=indent, ensure_ascii=False)

def write_raw_string(file_stream: TextIO, json_str: str) -> None:
    """
    [寫入]
    Writes a raw JSON string directly into an opened file stream.
    """
    file_stream.write(json_str)

# ==========================================
# 🆕 New Feature: Smart Path Handling
# ==========================================

def quick_read_json(file_path: str) -> Optional[Union[Dict, List]]:
    """
    A helper that handles opening and closing the file automatically.
    Pass a string path instead of a file object.
    """
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            return json.load(f)
    except Exception as e:
        print(f"Error reading JSON from {file_path}: {e}")
        return None

def quick_save_json(file_path: str, data: Any, indent: int = 4) -> bool:
    """
    A helper that saves data to a JSON file path directly.
    Ensures UTF-8 encoding and proper closing.
    """
    try:
        with open(file_path, 'w', encoding='utf-8') as f:
            json.dump(data, f, indent=indent, ensure_ascii=False)
        return True
    except Exception as e:
        print(f"Error saving JSON to {file_path}: {e}")
        return False
    


