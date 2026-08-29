#!/usr/bin/env python3
import pytest

from sorting.insertion_sort import sort_using_insertion
from sorting.selection_sort import sort_using_selection


@pytest.fixture(params=[sort_using_insertion, sort_using_selection])
def sort_func(request):
    """
    Fixture to parameterize tests with different sorting algorithms.

    Provides the following sorting functions sequentially to the tests:
    - `sort_using_insertion` (Insertion Sort)
    - `sort_using_selection` (Selection Sort)
    """
    return request.param


class TestSortingFunctions:
    def test_empty_list(self, sort_func):
        assert sort_func([]) == []

    def test_single_element(self, sort_func):
        assert sort_func([1]) == [1]

    def test_already_sorted(self, sort_func):
        assert sort_func([1, 2, 3, 4, 5]) == [1, 2, 3, 4, 5]

    def test_reverse_sorted(self, sort_func):
        assert sort_func([5, 4, 3, 2, 1]) == [1, 2, 3, 4, 5]

    def test_random_elements(self, sort_func):
        assert sort_func([3, 1, 4, 1, 5, 9, 2, 6, 5]) == [
            1, 1, 2, 3, 4, 5, 5, 6, 9]

    def test_duplicates(self, sort_func):
        assert sort_func([7, 3, 7, 3, 7, 3]) == [3, 3, 3, 7, 7, 7]

    def test_negative_numbers(self, sort_func):
        assert sort_func([-3, 5, -1, 0, 4, -8]) == [-8, -3, -1, 0, 4, 5]

    def test_all_same_elements(self, sort_func):
        assert sort_func([2, 2, 2, 2]) == [2, 2, 2, 2]
