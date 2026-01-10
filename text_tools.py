import base64
from typing import List
from deep_translator import GoogleTranslator

class TextUtility:
    """
    A utility class for text manipulation, translation, and encoding.
    """

    @staticmethod
    def repeat_text(text: str, times: int) -> str:
        """
        Repeats the given text a specified number of times.

        Args:
            text (str): The string to repeat.
            times (int): Number of times to repeat.

        Returns:
            str: The repeated string.
        """
        return text * times

    @staticmethod
    def to_uppercase(text: str) -> str:
        """Converts the string to uppercase."""
        return text.upper()

    @staticmethod
    def to_lowercase(text: str) -> str:
        """Converts the string to lowercase."""
        return text.lower()

    @staticmethod
    def capitalize_first(text: str) -> str:
        """Capitalizes the first character of the string."""
        return text.capitalize()

    @staticmethod
    def to_title_case(text: str) -> str:
        """Capitalizes the first letter of every word in the string."""
        return text.title()

    @staticmethod
    def get_char_count(text: str) -> int:
        """Returns the total number of characters in the string."""
        return len(text)

    @staticmethod
    def get_word_count(text: str) -> int:
        """Returns the total number of words in the string."""
        return len(text.split())

    @staticmethod
    def replace_text(text: str, old_val: str, new_val: str) -> str:
        """
        Replaces occurrences of a substring with a new string.

        Args:
            text (str): The original string.
            old_val (str): The substring to be replaced.
            new_val (str): The new substring.

        Returns:
            str: The modified string.
        """
        return text.replace(old_val, new_val)

    @staticmethod
    def find_keyword(text: str, keyword: str) -> int:
        """Returns the index of the first occurrence of the keyword, or -1 if not found."""
        return text.find(keyword)

    @staticmethod
    def swap_case(text: str) -> str:
        """Swaps uppercase to lowercase and vice versa."""
        return text.swapcase()

    @staticmethod
    def count_occurrences(text: str, sub: str, start: int = None, end: int = None) -> int:
        """Counts how many times a substring appears within a given range."""
        return text.count(sub, start, end)

    @staticmethod
    def split_text(text: str, separator: str = " ") -> List[str]:
        """Splits the string into a list based on a separator."""
        return text.split(separator)

    @staticmethod
    def join_list(data_list: List[str], separator: str = " ") -> str:
        """Joins a list of strings into a single string with a separator."""
        return separator.join(data_list)

    @staticmethod
    def is_alphanumeric(text: str) -> bool:
        """Checks if all characters in the string are letters or numbers."""
        return text.isalnum()

    @staticmethod
    def is_alpha(text: str) -> bool:
        """Checks if all characters in the string are letters."""
        return text.isalpha()

    @staticmethod
    def is_lower(text: str) -> bool:
        """Checks if all cased characters in the string are lowercase."""
        return text.islower()

    @staticmethod
    def is_upper(text: str) -> bool:
        """Checks if all cased characters in the string are uppercase."""
        return text.isupper()

    @staticmethod
    def is_digit(text: str) -> bool:
        """Checks if all characters in the string are digits."""
        return text.isdigit()

    @staticmethod
    def is_title(text: str) -> bool:
        """Checks if the string follows title case rules."""
        return text.istitle()

    @staticmethod
    def translate_text(text: str, source: str = "auto", target: str = "zh-TW") -> str:
        """
        Translates a single string using Google Translator.

        Args:
            text (str): The text to translate.
            source (str): Source language code.
            target (str): Target language code.

        Returns:
            str: The translated text.
        """
        try:
            return GoogleTranslator(source=source, target=target).translate(text)
        except Exception as e:
            return f"Translation error: {e}"

    @staticmethod
    def translate_batch(text_list: List[str], source: str = "auto", target: str = "zh-TW") -> List[str]:
        """Translates a list of strings."""
        try:
            return GoogleTranslator(source=source, target=target).translate_batch(text_list)
        except Exception as e:
            return [f"Translation error: {e}"] * len(text_list)

    @staticmethod
    def string_to_base64(text: str) -> str:
        """Encodes a UTF-8 string into a Base64 string."""
        text_bytes = text.encode("utf-8")
        base64_bytes = base64.b64encode(text_bytes)
        return base64_bytes.decode("utf-8")

    @staticmethod
    def base64_to_string(base64_text: str) -> str:
        """Decodes a Base64 string back to its original UTF-8 string."""
        base64_bytes = base64_text.encode("utf-8")
        original_bytes = base64.b64decode(base64_bytes)
        return original_bytes.decode("utf-8")

# Example Usage:
# if __name__ == "__main__":
#     util = TextUtility()
#     print(util.to_uppercase("hello"))