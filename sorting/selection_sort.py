#!/usr/bin/env python3

def sort_using_selection(numbers: list[int]) -> list[int]:
    """
    Sorts a list of integers in ascending order using the selection sort algorithm.

    Logic:
        The algorithm divides the input list into two parts: 
        a sorted sublist of items which is built up from left to right 
        at the front (left) of the list, and a sublist of the remaining 
        unsorted items that occupy the rest of the list.

        Initially, the sorted sublist is empty and the unsorted sublist 
        is the entire input list. The algorithm proceeds by finding 
        the smallest element in the unsorted sublist, exchanging (swapping) 
        it with the leftmost unsorted element (putting it in sorted order),
        and moving the sublist boundaries one element to the right.

    Time Complexity:
        - Best, Average, and Worst Case: O(n^2) where n is the length of the list,
          because it always scans the remaining unsorted portion to find the minimum.

    Space Complexity:
        - O(1) auxiliary space, as the sorting is done in-place.

    Args:
        numbers (list[int]): The list of integers to be sorted.

    Returns:
        list[int]: The same list sorted in ascending order.
    """
    arr_len = len(numbers)
    for i in range(arr_len):
        # assume the smalest num is at the current position
        min_index = i

        # loop over the rest of the elements
        for j in range(i, arr_len):
            if numbers[min_index] > numbers[j]:
                min_index = j
        # swap
        numbers[i], numbers[min_index] = numbers[min_index], numbers[i]

    return numbers


if __name__ == "__main__":
    # unsorted_list = [int(x) for x in input().split() if x.isdigit()]
    unsorted_list = [5, 3, 1, 2, 4]
    # print(unsorted_list)
    res = sort_using_selection(unsorted_list)
    print(res)
