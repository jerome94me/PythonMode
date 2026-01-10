import random
from typing import Any, Union, List, Tuple

class RandomUtility:
    """
    A utility class for various random sampling and generation tasks.
    """

    @staticmethod
    def get_random_int(min_val: int, max_val: int) -> int:
        """
        Returns a random integer between min_val and max_val (inclusive).

        Args:
            min_val (int): The lower bound of the random range (inclusive).
            max_val (int): The upper bound of the random range (inclusive).

        Returns:
            int: A random integer within the range [min_val, max_val].
        """
        # random.randint(a, b) includes both a and b
        return random.randint(min_val, max_val)

    @staticmethod
    def get_random_float(min_val: Union[int, float], max_val: Union[int, float]) -> float:
        """
        Returns a random floating-point number between min_val and max_val.

        Args:
            min_val (Union[int, float]): The lower bound of the random range.
            max_val (Union[int, float]): The upper bound of the random range.

        Returns:
            float: A random float within the range [min_val, max_val].
        """
        # random.uniform(a, b) typically includes a and b depending on rounding
        return random.uniform(min_val, max_val)

    @staticmethod
    def sample_multiple(data_list: Union[List, Tuple], count: int) -> List:
        """
        Randomly picks multiple unique items from a list or tuple.
        
        Args:
            data_list (Union[List, Tuple]): The source list or tuple to sample from.
            count (int): The number of unique items to retrieve.

        Returns:
            List: A new list containing the randomly sampled items.
        """
        return random.sample(data_list, count)

    @staticmethod
    def choice_single(data_list: Union[List, Tuple]) -> Any:
        """
        Randomly picks a single item from a list or tuple.
        
        Args:
            data_list (Union[List, Tuple]): The source list or tuple to pick from.

        Returns:
            Any: A single randomly selected item.
        """
        return random.choice(data_list)

    @staticmethod
    def shuffle_list(data_list: Union[List, Tuple]) -> List:
        """
        Shuffles the items in a list or tuple and returns them as a new list.
        
        Args:
            data_list (Union[List, Tuple]): The source list or tuple to be shuffled.

        Returns:
            List: A new list containing the shuffled items.
        """
        # random.shuffle() only works in-place on lists, so we create a copy first
        shuffled_list = list(data_list)
        random.shuffle(shuffled_list)
        return shuffled_list

# Example Usage:
# if __name__ == "__main__":
#     rand = RandomUtility()
#     print(f"Random Int: {rand.get_random_int(1, 10)}")