#!/usr/bin/env python3


def sort_using_merge(numbers: list[int]) -> list[int]:
    """
    Sorts a list of integers in ascending order using the merge sort algorithm.

    Logic:
        Merge sort is a divide-and-conquer algorithm. It recursively divides the
        input list into two halves until each sublist contains a single element
        (which is naturally sorted). Then, it repeatedly merges the sublists
        back together by comparing the elements at the front of each sublist and
        appending the smaller one to a new sorted list, until all elements are merged.

    Time Complexity:
        - Best, Average, and Worst Case: O(n log n) where n is the length of the list.
          The list is always divided in half (log n splits) and merging takes linear time (n).

    Space Complexity:
        - O(n) auxiliary space, as new lists are created to store the left, right,
          and merged sublists during the recursive calls.

    Args:
        numbers (list[int]): The list of integers to be sorted.

    Returns:
        list[int]: A new list containing the elements sorted in ascending order.
    """
    nums_len = len(numbers)
    if nums_len <= 1:
        return numbers

    mid = nums_len // 2
    r_list = sort_using_merge(numbers[mid:])
    l_list = sort_using_merge(numbers[:mid])

    left_ptr, right_ptr = 0, 0
    sorted_list = []

    while left_ptr < mid or right_ptr < nums_len - mid:
        if left_ptr == mid:
            # left list is empty, take elem from right list
            sorted_list.append(r_list[right_ptr])
            right_ptr += 1
        elif right_ptr == (nums_len - mid):
            # right list is empty, take elem from left list
            sorted_list.append(l_list[left_ptr])
            left_ptr += 1
        elif l_list[left_ptr] <= r_list[right_ptr]:
            # take smallest elem from the left list
            sorted_list.append(l_list[left_ptr])
            left_ptr += 1
        else:
            # take the smallest elem from the right list
            sorted_list.append(r_list[right_ptr])
            right_ptr += 1

    return sorted_list


if __name__ == "__main__":

    # unsorted_list = [int(x) for x in input().split()]
    unsorted_list = [15, 22, 1, 3, 2, 7, 8, 21, 12, 9, 5, 4, 6]
    # unsorted_list = [3, 1, 2]
    res = sort_using_merge(unsorted_list)
    print(" ".join(map(str, res)))



