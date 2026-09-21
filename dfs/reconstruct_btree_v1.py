#!/usr/bin/env python3

from typing import Optional
from dfs.utils import Node


def build_recursive(preorder: list[int], preord_index: int, inord_start: int, size: int, value_to_index: dict) -> Optional[Node]:

    if size <= 0:
        return None

    root_value = preorder[preord_index]
    inorder_root_index = value_to_index[root_value]
    # left_subtree_size = inorder_root_index - inord_start

    left_inord_start = inord_start
    right_inord_start = inorder_root_index + 1
    #
    left_subtree_size = inorder_root_index - inord_start
    right_subtree_size = size - 1 - left_subtree_size
    #
    left_preord_index = preord_index + 1
    right_preord_index = preord_index + 1 + left_subtree_size

    left_child = build_recursive(
        preorder, left_preord_index,  left_inord_start, left_subtree_size,  value_to_index)
    right_child = build_recursive(
        preorder, right_preord_index, right_inord_start, right_subtree_size, value_to_index)

    return Node(root_value, left_child, right_child)


def construct_binary_tree(preorder: list[int], inorder: list[int]) -> Optional[Node]:
    value_to_index = {val: idx for idx, val in enumerate(inorder)}
    return build_recursive(preorder, 0, 0, len(preorder), value_to_index)

