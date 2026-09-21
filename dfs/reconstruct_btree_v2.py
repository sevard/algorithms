#!/usr/bin/env python3

from typing import List, Optional
from dfs.utils import Node, pretty_print_tree

"""
    Core Concepts
    1) Preorder Traversal Pattern ([Root → Left → Right]): 
        The first element of preorder is always the root of the tree/subtree. 
        As we traverse the tree, the global pointer pre_idx simply moves 
        from left to right in the preorder list to retrieve the next root node.

    2) Inorder Traversal Pattern ([Left → Root → Right]):
        Once we know the root's value, we locate its index (root_in_idx) in the inorder list.
        Elements to the left of root_in_idx in the inorder list form the left subtree.
        Elements to the right of root_in_idx form the right subtree.
"""

def construct_binary_tree(preorder: List[int], inorder: List[int]) -> Optional[Node]:
    """
    Builds a binary tree from preorder and inorder traversals.
    Time Complexity: O(n)
    Space Complexity: O(n)
    """
    index_map = {val: i for i, val in enumerate(inorder)}
    pre_idx = 0

    def build(in_start: int, in_end: int) -> Optional[Node]:
        nonlocal pre_idx

        # If the range boundaries cross, 
        # it means the current subtree is empty
        if in_start > in_end:
            return None

        root_val = preorder[pre_idx]
        root = Node(root_val)
        pre_idx += 1

        # Root index in inorder
        root_in_idx = index_map[root_val]

        # Build left and right subtrees
        root.left = build(in_start, root_in_idx - 1)
        root.right = build(root_in_idx + 1, in_end)

        return root

    return build(0, len(inorder) - 1)


if __name__ == "__main__":
    preorder = [3, 9, 20, 15, 7]
    inorder = [9, 3, 15, 20, 7]

    res = construct_binary_tree(preorder, inorder)
    print("Preorder:", preorder)
    print("Inorder: ", inorder)
    print("\nResulting Tree Structure:")
    # Using the print_tree utility for better visualization
    pretty_print_tree(res)
