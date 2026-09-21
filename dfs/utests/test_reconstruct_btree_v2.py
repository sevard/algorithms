#!/usr/bin/env python3

from typing import Optional
from dfs.utils import Node
from dfs.reconstruct_btree_v2 import construct_binary_tree


def get_preorder(node: Optional[Node]) -> list:
    res = []

    def dfs(curr):
        if not curr:
            return
        res.append(curr.val)
        dfs(curr.left)
        dfs(curr.right)

    dfs(node)
    return res


def get_inorder(node: Optional[Node]) -> list:
    res = []

    def dfs(curr):
        if not curr:
            return
        dfs(curr.left)
        res.append(curr.val)
        dfs(curr.right)

    dfs(node)
    return res


def assert_trees_equal(t1: Optional[Node], t2: Optional[Node]):
    if not t1 and not t2:
        return
    if not t1 or not t2:
        raise AssertionError("Trees do not have the same structure")
    assert t1.val == t2.val
    assert_trees_equal(t1.left, t2.left)
    assert_trees_equal(t1.right, t2.right)


def test_example_case():
    preorder = [3, 9, 20, 15, 7]
    inorder = [9, 3, 15, 20, 7]

    # Expected manual tree
    #      3
    #     / \
    #    9  20
    #      /  \
    #     15   7
    expected = Node(3, Node(9), Node(20, Node(15), Node(7)))

    result = construct_binary_tree(preorder, inorder)

    assert_trees_equal(result, expected)
    assert get_preorder(result) == preorder
    assert get_inorder(result) == inorder


def test_empty_tree():
    preorder = []
    inorder = []

    result = construct_binary_tree(preorder, inorder)
    assert result is None


def test_single_element():
    preorder = [1]
    inorder = [1]

    expected = Node(1)
    result = construct_binary_tree(preorder, inorder)

    assert_trees_equal(result, expected)
    assert get_preorder(result) == preorder
    assert get_inorder(result) == inorder


def test_left_skewed_tree():
    preorder = [1, 2, 3]
    inorder = [3, 2, 1]

    # Expected:
    #      1
    #     /
    #    2
    #   /
    #  3
    expected = Node(1, Node(2, Node(3)))
    result = construct_binary_tree(preorder, inorder)

    assert_trees_equal(result, expected)
    assert get_preorder(result) == preorder
    assert get_inorder(result) == inorder


def test_right_skewed_tree():
    preorder = [1, 2, 3]
    inorder = [1, 2, 3]

    # Expected:
    #  1
    #   \
    #    2
    #     \
    #      3
    expected = Node(1, None, Node(2, None, Node(3)))
    result = construct_binary_tree(preorder, inorder)

    assert_trees_equal(result, expected)
    assert get_preorder(result) == preorder
    assert get_inorder(result) == inorder


def test_balanced_symmetric_tree():
    preorder = [1, 2, 4, 5, 3, 6, 7]
    inorder = [4, 2, 5, 1, 6, 3, 7]

    # Expected:
    #       1
    #     /   \
    #    2     3
    #   / \   / \
    #  4   5 6   7
    expected = Node(1, Node(2, Node(4), Node(5)),
                    Node(3, Node(6), Node(7)))
    result = construct_binary_tree(preorder, inorder)

    assert_trees_equal(result, expected)
    assert get_preorder(result) == preorder
    assert get_inorder(result) == inorder
