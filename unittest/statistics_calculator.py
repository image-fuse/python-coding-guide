import statistics
from typing import List, Tuple, Union

def calculate_statistics(data: list[float]) -> dict:
    """
    Calculate mean, median, and standard deviation of numerical data.

    Args:
        data (list[float]): List of numerical data.

    Returns:
        dict: A dictionary containing calculated mean, median, and standard deviation.
    """
    if not data:
        raise ValueError("Input data cannot be empty")

    mean = sum(data) / len(data)
    median = statistics.median(data)

    # Calculate standard deviation only if there are at least two data points
    if len(data) >= 2:
        std_dev = statistics.stdev(data)
    else:
        std_dev = 0

    result = {"mean": mean, "median": median, "std_dev": std_dev}

    return result
