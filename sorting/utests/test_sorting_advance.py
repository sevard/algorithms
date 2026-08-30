#!/usr/bin/env python3
import pytest

from sorting.quick_sort import sort


@pytest.fixture(params=[sort])
def sort_func(request):
    """
    Fixture to parameterize tests with different advanced sorting algorithms.

    Provides the following sorting functions sequentially to the tests:
    - `sort` (Quick Sort in-place)
    """
    return request.param


class TestSortingFunctions:
    def test_empty_list(self, sort_func):
        test_list = []
        sort_func(test_list)
        assert test_list == []

    def test_single_element(self, sort_func):
        test_list = [1]
        sort_func(test_list)
        assert test_list == [1]

    def test_already_sorted(self, sort_func):
        test_list = [1, 2, 3, 4, 5]
        sort_func(test_list)
        assert test_list == [1, 2, 3, 4, 5]

    def test_reverse_sorted(self, sort_func):
        test_list = [5, 4, 3, 2, 1]
        sort_func(test_list)
        assert test_list == [1, 2, 3, 4, 5]

    def test_random_elements(self, sort_func):
        test_list = [3, 1, 4, 1, 5, 9, 2, 6, 5]
        sort_func(test_list)
        assert test_list == [1, 1, 2, 3, 4, 5, 5, 6, 9]

    def test_duplicates(self, sort_func):
        test_list = [7, 3, 7, 3, 7, 3]
        sort_func(test_list)
        assert test_list == [3, 3, 3, 7, 7, 7]

    def test_negative_numbers(self, sort_func):
        test_list = [-3, 5, -1, 0, 4, -8]
        sort_func(test_list)
        assert test_list == [-8, -3, -1, 0, 4, 5]

    def test_all_same_elements(self, sort_func):
        test_list = [2, 2, 2, 2]
        sort_func(test_list)
        assert test_list == [2, 2, 2, 2]
