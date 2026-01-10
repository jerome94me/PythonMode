from typing import Any, Dict, Union
import psutil

class NotALaptopError(Exception):
    """Raised when battery information is requested in a non-laptop environment."""
    pass

class HardwareMonitor:
    def __init__(self, is_laptop: bool = False) -> None:
        """
        Initialize the monitor.
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