#!/usr/bin/env python3

from sorting.insertion_sort import sort_using_insertion


def test_empty_list():
    assert sort_using_insertion([]) == []


def test_single_element():
    assert sort_using_insertion([1]) == [1]


def test_already_sorted():
    assert sort_using_insertion([1, 2, 3, 4, 5]) == [1, 2, 3, 4, 5]


def test_reverse_sorted():
    assert sort_using_insertion([5, 4, 3, 2, 1]) == [1, 2, 3, 4, 5]


def test_random_elements():
    assert sort_using_insertion([3, 1, 4, 1, 5, 9, 2, 6, 5]) == [
        1, 1, 2, 3, 4, 5, 5, 6, 9]


def test_duplicates():
    assert sort_using_insertion([7, 3, 7, 3, 7, 3]) == [3, 3, 3, 7, 7, 7]


def test_negative_numbers():
    assert sort_using_insertion([-3, 5, -1, 0, 4, -8]) == [-8, -3, -1, 0, 4, 5]


def test_all_same_elements():
    assert sort_using_insertion([2, 2, 2, 2]) == [2, 2, 2, 2]
