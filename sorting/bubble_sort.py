#!/usr/bin/env python3


def sort_using_bubble(numbers: list[int]) -> list[int]:
    """
    Sorts a list of integers in ascending order using the bubble sort algorithm.

    Logic:
        The algorithm repeatedly steps through the list, compares adjacent elements,
        and swaps them if they are in the wrong order. The pass through the list is
        repeated until no swaps are needed, which indicates that the list is sorted.
        This implementation includes an optimization to stop early if no swaps occur
        during a pass, and it ignores the end of the list which is already sorted
        after each iteration.

    Time Complexity:
        - Best Case: O(n) when the list is already sorted (due to the early exit flag).
        - Average/Worst Case: O(n^2) where n is the length of the list, 
          when elements are completely unsorted or in reverse order.

    Space Complexity:
        - O(1) auxiliary space, as the sorting is done in-place.

    Args:
        numbers (list[int]): The list of integers to be sorted.

    Returns:
        list[int]: The same list sorted in ascending order.
    """
    nums_len = len(numbers)

    for i in range(nums_len - 1):
        swapped = False

        for j in range(nums_len - 1 - i):
            if numbers[j] > numbers[j + 1]:
                # swap
                numbers[j], numbers[j + 1] = numbers[j + 1], numbers[j]
                swapped = True
        if not swapped:
            break

    return numbers
