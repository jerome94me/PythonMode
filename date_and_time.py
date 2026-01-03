import calendar
from datetime import datetime, date, timedelta

# ==========================================
# Global Constants (Standard English Names)
# ==========================================
WEEKDAY_NAMES = list(calendar.day_name)
WEEKDAY_ABBR = list(calendar.day_abbr)
MONTH_NAMES = list(calendar.month_name)
MONTH_ABBR = list(calendar.month_abbr)

# ------------------------------------------
# Core Time Retrieval
# ------------------------------------------

def get_now_full() -> datetime:
    """
    Retrieves the complete datetime object (Local Time).
    
    Returns:
        datetime: Current date and time object.
    """
    return datetime.now()

def get_today() -> date:
    """
    Retrieves the date object (Year, Month, Day).
    
    Returns:
        date: Current date object.
    """
    return date.today()

def format_now(format_str: str = "%Y-%m-%d %H:%M:%S") -> str:
    """
    Formats the current time into a specified string format.
    
    Args:
        format_str (str): Format codes (e.g., %Y: Year, %H: Hour).
    
    Returns:
        str: Formatted date-time string.
    """
    return datetime.now().strftime(format_str)

# ------------------------------------------
# Time Calculations & Comparison
# ------------------------------------------

def get_time_diff(dt_end: datetime, dt_start: datetime) -> timedelta:
    """Calculates the difference (timedelta) between two datetime objects."""
    return dt_end - dt_start

def compare_dates(dt1: datetime, dt2: datetime) -> str:
    """
    Compares two datetime objects and returns their chronological relationship.
    """
    if dt1 > dt2:
        return f"{dt1} is AFTER {dt2}"
    elif dt1 < dt2:
        return f"{dt1} is BEFORE {dt2}"
    else:
        return f"{dt1} is the SAME as {dt2}"

def parse_string_to_datetime(dt_string: str, format_str: str = "%Y-%m-%d %H:%M:%S") -> datetime:
    """Converts a formatted string back into a datetime object."""
    return datetime.strptime(dt_string, format_str)

def is_leap_year(year: int) -> bool:
    """Checks if a given year is a leap year."""
    return (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0)

# ------------------------------------------
# New Features Added for You
# ------------------------------------------

def get_timestamp() -> float:
    """Returns the current Unix timestamp (Seconds since 1970-01-01)."""
    return datetime.now().timestamp()

def offset_time(dt: datetime, days: int = 0, hours: int = 0, minutes: int = 0) -> datetime:
    """
    Adds or subtracts time from a given datetime.
    Example: offset_time(now, days=-1) gets yesterday's time.
    """
    return dt + timedelta(days=days, hours=hours, minutes=minutes)