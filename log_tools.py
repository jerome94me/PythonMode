import os
from typing import Any, Dict, Union, Callable
import psutil
import keyboard
from loguru import logger

class NotALaptopError(Exception):
    """Raised when battery information is requested in a non-laptop environment."""
    pass

class LogManager:
    """
    Custom logging management utility wrapping the Loguru library.
    Handles directory creation, rotation, retention, and custom formatting.
    """
    def __init__(self, log_dir: str = "logs", log_name: str = "app.log") -> None:
        """
        Initialize the log manager.
        :param log_dir: Directory where log files will be stored.
        :param log_name: The name of the primary log file.
        """
        if not os.path.exists(log_dir):
            os.makedirs(log_dir)
        
        self.log_path = os.path.join(log_dir, log_name)
        self._configure_loguru()

    def _configure_loguru(self) -> None:
        """Configures Loguru handlers with rotation, retention, and compression."""
        # Custom format including process and thread IDs for better debugging
        log_format = (
            "<green>{time:YYYY-MM-DD HH:mm:ss.SSS}</green> | "
            "<level>{level: <8}</level> | "
            "<cyan>{name}</cyan>:<cyan>{function}</cyan>:<cyan>{line}</cyan> - "
            "<level>{message}</level>"
        )

        # Add file sink with optimized settings
        logger.add(
            self.log_path,
            format=log_format,
            rotation="500 MB",     # Auto-rotate when file size reaches 500MB
            retention="10 days",   # Keep logs for 10 days
            compression="zip",     # Compress old log files
            level="DEBUG",         # Record everything from DEBUG level upwards
            encoding="utf-8",      # Ensure character compatibility
            enqueue=True,          # Thread-safe and asynchronous
            backtrace=True,        # Detailed stack trace
            diagnose=True          # Show variable values in stack trace
        )

    def info(self, message: str) -> None:
        """Log an informational message."""
        logger.info(message)

    def success(self, message: str) -> None:
        """Log a success message (Loguru specific level)."""
        logger.success(message)

    def warning(self, message: str) -> None:
        """Log a warning message."""
        logger.warning(message)

    def error(self, message: str, exception: Exception = None) -> None:
        """
        Log an error message with optional exception details.
        :param message: The error description.
        :param exception: The exception object for backtrace recording.
        """
        if exception:
            logger.exception(f"{message}: {str(exception)}")
        else:
            logger.error(message)

    def debug(self, message: str) -> None:
        """Log a debug message."""
        logger.debug(message)

    def critical(self, message: str) -> None:
        """Log a critical failure message."""
        logger.critical(message)