from typing import Any, Dict, Union, Callable
import psutil
import keyboard

class NotALaptopError(Exception):
    """Raised when battery information is requested in a non-laptop environment."""
    pass

class HardwareMonitor:
    def __init__(self, is_laptop: bool = False) -> None:
        """
        Initialize the hardware monitor.
        :param is_laptop: Boolean flag to indicate if the environment is a laptop.
        """
        self.is_laptop = is_laptop

    def get_cpu_usage(self, interval: Union[int, float, None] = 0.5) -> float:
        """
        Get the CPU usage percentage.
        :param interval: Sampling interval in seconds.
        """
        return psutil.cpu_percent(interval)

    def get_memory_info(self, as_dict: bool = True) -> Union[Dict[str, Any], Any]:
        """
        Get memory status (total, available, percent, used, free).
        :param as_dict: Whether to return the result as a dictionary.
        """
        mem = psutil.virtual_memory()
        return mem._asdict() if as_dict else mem

    def get_disk_info(self, path: str = "/", as_dict: bool = True) -> Union[Dict[str, Any], Any]:
        """
        Get disk usage for a specific path.
        :param path: The file system path to check.
        :param as_dict: Whether to return the result as a dictionary.
        """
        disk = psutil.disk_usage(path)
        return disk._asdict() if as_dict else disk

    def get_battery_info(self) -> Any:
        """
        Get battery level and charging status.
        Raises NotALaptopError if the instance is not configured as a laptop.
        """
        battery = psutil.sensors_battery()
        if self.is_laptop and battery:
            return battery._asdict()
        elif not self.is_laptop:
            # Custom exception for non-laptop environments
            raise NotALaptopError("Error: This computer is configured as 'Not a Laptop'. Battery info unavailable.")
        else:
            return "Battery not detected"

class InputMonitor:
    """Utility class for monitoring and simulating keyboard inputs."""

    @staticmethod
    def on_key_press(key: str, callback: Callable) -> None:
        """
        Listen for a single key press event.
        :param key: Name of the key to listen for (e.g., 'a', 'space').
        :param callback: Function to execute on press.
        """
        keyboard.on_press_key(key, callback)

    @staticmethod
    def on_key_release(key: str, callback: Callable) -> None:
        """
        Listen for a single key release event.
        :param key: Name of the key.
        :param callback: Function to execute on release.
        """
        keyboard.on_release_key(key, callback)

    @staticmethod
    def on_any_key_press(callback: Callable) -> None:
        """
        Listen for any key press event.
        :param callback: Callback function receiving the event object.
        """
        keyboard.on_press(callback)

    @staticmethod
    def add_hotkey(hotkey: str, callback: Callable) -> Any:
        """
        Set up a hotkey listener (e.g., 'ctrl+shift+a').
        :param hotkey: The combination string.
        :param callback: Function to trigger.
        :return: Hotkey ID for removal.
        """
        return keyboard.add_hotkey(hotkey, callback)

    @staticmethod
    def block_key(key: str) -> None:
        """
        Blocks a specific key from being processed by the system.
        :param key: The key to block.
        """
        keyboard.block_key(key)

    @staticmethod
    def press_key(key: str) -> None:
        """
        Simulate pressing a key (without releasing).
        :param key: The key to press.
        """
        keyboard.press(key)

    @staticmethod
    def release_key(key: str) -> None:
        """
        Simulate releasing a key.
        :param key: The key to release.
        """
        keyboard.release(key)

    @staticmethod
    def send_key(key: str) -> None:
        """
        Simulate a full key stroke (press and release).
        :param key: The key to send.
        """
        keyboard.send(key)

    @staticmethod
    def is_key_pressed(key: str) -> bool:
        """
        Check if a specific key is currently being held down.
        :param key: The key to check.
        :return: True if pressed, False otherwise.
        """
        return keyboard.is_pressed(key)

    @staticmethod
    def on_long_press(key: str, callback: Callable) -> None:
        """
        Triggers a callback repeatedly while a key is held down.
        :param key: The key to monitor.
        :param callback: Function to repeat.
        """
        def wrapper():
            if keyboard.is_pressed(key):
                callback()
        keyboard.on_press_key(key, lambda _: wrapper())

    @staticmethod
    def remove_hotkey(hotkey_id: Any) -> None:
        """
        Remove a specific hotkey or listener.
        :param hotkey_id: The ID returned by add_hotkey.
        """
        keyboard.remove_hotkey(hotkey_id)

    @staticmethod
    def stop_all_listeners() -> None:
        """Removes all keyboard hooks and listeners."""
        keyboard.unhook_all()