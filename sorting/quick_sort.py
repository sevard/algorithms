#!/usr/bin/env python3


def _sort_list_interval(numbers: list[int], start: int, end: int) -> None:
    """
    Recursively sorts a sub-interval of the list in-place.

    Logic:
    - Selects the last element of the interval as the pivot.
    - Uses a two-pointer approach to partition the interval such that 
      elements less than the pivot are on the left, and elements greater 
      or equal to the pivot are on the right.
    - Swaps the pivot into its final sorted position.
    - Recursively sorts the left and right sub-intervals.

    Complexity:
    - Time Complexity: O(N log N) on average, O(N^2) worst case (e.g. already sorted).
    - Space Complexity: O(1) auxiliary space, O(N) max call stack depth due to recursion.
    """

    # If segment is 1 or 0, it is sorted
    if end - start <= 1:
        return

    # set pivot to be the last elem
    pivot = numbers[end - 1]
    start_ptr, end_ptr = start, end - 1

    # Start partitioning
    while start_ptr < end_ptr:

        # find element from left that is greater than pivot
        while numbers[start_ptr] < pivot and start_ptr < end_ptr:
            start_ptr += 1
        # find element from right that is less or equal pivot
        while numbers[end_ptr] >= pivot and start_ptr < end_ptr:
            end_ptr -= 1

        # if pointers have not met, swap the left and right values
        if start_ptr < end_ptr:
            numbers[start_ptr], numbers[end_ptr] = numbers[end_ptr], numbers[start_ptr]

    # Place pivot in its final position
    numbers[start_ptr], numbers[end - 1] = numbers[end - 1], numbers[start_ptr]

    _sort_list_interval(numbers, start, start_ptr)
    _sort_list_interval(numbers, start_ptr + 1, end)
    return


def sort(list_of_numbers: list[int]) -> None:
    """
    Sorts a list of integers in-place using the Quick Sort algorithm.
    Modifies the input list and returns None.

    Memory Efficiency:
    This implementation is more memory efficient compared to the v2 version 
    because it partitions the array in-place rather than allocating new lists 
    at each recursive step (O(1) auxiliary space vs O(N log N)).

    Pivot Selection:
    This algorithm selects the last element as the pivot. While simple, this 
    strategy leads to O(N^2) worst-case time complexity if the input array is 
    already sorted, reverse-sorted, or contains all identical elements.
    """
    _sort_list_interval(list_of_numbers, 0, len(list_of_numbers))
    return


def _sort_v2(arr: list[int]) -> list[int]:
    """
    Sorts a list of integers using the Quick Sort algorithm.

    Logic:
        - Selects the middle element as the pivot.
        - Partitions the array into three separate lists:   
            elements less than the pivot
            elements equal to the pivot
            elements greater than the pivot
        - Recursively sorts the 'less than' and 'greater than' lists and concatenates the results.

    Complexity:
    - Time Complexity: 
        - Average/Best Case: O(N log N)
        - Worst Case: O(N^2) (occurs when the pivot is consistently the smallest or largest element)
    - Space Complexity: 
        - Average Case: O(N log N) due to the creation of new lists at each recursive call depth.
        - Worst Case: O(N^2) auxiliary space.

    Args:
        arr: The list of integers to sort.

    Returns:
        A new sorted list of integers.
    """
    if len(arr) <= 1:
        return arr  # Base case

    # Choose middle element as pivot
    pivot = arr[len(arr) // 2]

    left = [x for x in arr if x < pivot]    # Elements less than pivot
    middle = [x for x in arr if x == pivot]  # Elements equal to pivot
    right = [x for x in arr if x > pivot]   # Elements greater than pivot

    return _sort_v2(left) + middle + _sort_v2(right)


if __name__ == "__main__":
    test_list_one = [3, 12, 9, 2, 11, 1, 7, 6, 5, 4]
    test_list_two = [3, 12, 9, 2, 11, 1, 7, 6, 5, 4]

    sort(test_list_one)
    print("sort version 1", test_list_one)
    print("sort version 2", _sort_v2(test_list_two))
