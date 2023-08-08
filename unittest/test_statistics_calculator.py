import unittest
from statistics_calculator import calculate_statistics
from typing import List, Dict, Union

class TestStatisticsCalculator(unittest.TestCase):

    def test_empty_list(self) -> None:
        """
        Test calculating statistics for an empty list.
        """
        with self.assertRaises(ValueError):
            calculate_statistics([])

    def test_single_element(self) -> None:
        """
        Test calculating statistics for a list with a single element.
        """
        result: Dict[str, Union[float, int]] = calculate_statistics([5])
        self.assertEqual(result["mean"], 5)
        self.assertEqual(result["median"], 5)
        self.assertEqual(result["std_dev"], 0)

    def test_even_number_of_elements(self) -> None:
        """
        Test calculating statistics for a list with an even number of elements.
        """
        data: List[Union[int, float]] = [10, 20, 30, 40]
        result: Dict[str, Union[float, int]] = calculate_statistics(data)
        self.assertEqual(result["mean"], 25)
        self.assertEqual(result["median"], 25)
        self.assertAlmostEqual(result["std_dev"], 12.91, places=2)

    def test_odd_number_of_elements(self) -> None:
        """
        Test calculating statistics for a list with an odd number of elements.
        """
        data: List[Union[int, float]] = [15, 25, 35, 45, 55]
        result: Dict[str, Union[float, int]] = calculate_statistics(data)
        self.assertEqual(result["mean"], 35)
        self.assertEqual(result["median"], 35)
        self.assertAlmostEqual(result["std_dev"], 15.8113, places=2)

if __name__ == '__main__':
    unittest.main()
