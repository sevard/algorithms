#!/usr/bin/env python3


def sort_using_insertion(numbers: list[int]) -> list[int]:
    """
    Sorts a list of integers in ascending order using the insertion sort algorithm.

    Logic:
        The algorithm builds the sorted array one element at a time. 
        It iterates through the list, and for each element, 
        it compares it with the previous elements, swapping them 
        if they are out of order, until the element is in its correct 
        sorted position relative to the already processed elements.

    Time Complexity:
        - Best Case: O(n) when the list is already sorted.
        - Average/Worst Case: O(n^2) where n is the length of the list.

    Space Complexity:
        - O(1) auxiliary space, as the sorting is done in-place.

    Args:
        numbers (list[int]): The list of integers to be sorted.

    Returns:
        list[int]: The same list sorted in ascending order.
    """
    nums_len = len(numbers)
    for indx in range(nums_len):

        curr = indx

        # gets the smallest element and inserts it at current index
        while curr > 0 and numbers[curr] < numbers[curr - 1]:
            # swaps current smaller element with the element before it
            numbers[curr], numbers[curr - 1] = numbers[curr - 1], numbers[curr]
            curr -= 1

    return numbers


if __name__ == "__main__":

    unsorted_list = [int(x) for x in input().split()]
    res = sort_using_insertion(unsorted_list)
    print(" ".join(map(str, res)))
