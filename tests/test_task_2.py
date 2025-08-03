"""Test cases for the BubbleSort class in task_2.py"""

from src.task_2 import BubbleSort

EXPECTED_SORTED_SET = [0, 1, 2, 3, 4, 5, 6, 7]


def test_bubble_sort():
    # Arrange
    arr = [5, 3, 2, 4, 7, 1, 0, 6]

    # Act
    bubble_sort = BubbleSort(arr)
    sorted_arr = bubble_sort.sort()

    # Assert
    assert sorted_arr == EXPECTED_SORTED_SET
