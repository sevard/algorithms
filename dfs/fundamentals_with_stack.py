#!/usr/bin/env python3

from typing import Optional
from collections import deque
from utils import Node, build_tree


def in_order_traversal(root: Optional[Node]) -> None:
    """ Visits the left branch first, then current node,
     and finally the right branch.  <-, self , -> """
    if not root:
        return root

    stack = deque()
    stack.append(root)

    while stack:
        node = stack.pop()

        if node.right:
            stack.append(node.right)
        if node.left:
            print(node.left.val)
        print(node.val)
    return


def pre_order_traversal(root: Optional[Node]) -> None:
    """ Visits current node first, then left subtree, 
        and finally the right subtree. self, <-, -> """
    if not root:
        return root

    stack = deque()
    stack.append(root)

    while stack:
        node = stack.pop()
        print(node.val)
        if node.right:
            stack.append(node.right)
        if node.left:
            stack.append(node.left)
    return


def post_order_traversal(root: Node) -> None:
    """ Visits left subtree first, then right subtree,
        and finally current node. <- , ->, self """
    return


def find_target_value(root: Optional[Node], target) -> Optional[int]:
    """ 
    Searches for target value in tree using DFS approach without recursion 
    Implemented using stack data structure, and Pre-Order traversal. 

    Parameters:
        root: Node - root of the tree
        target: int - value to search for
    """

    stack = deque()
    stack.append(root)

    while stack:
        node = stack.pop()
        if node.val == target:
            return target

        if node.right:
            stack.append(node.right)
        if node.left:
            stack.append(node.left)
    return


if __name__ == "__main__":
    # inp = "5 4 3 x x 8 x x 6 x x"
    inp = "1 2 3 x 5 x x 4 x x 6 x x"
    # root = build_tree(iter(input().split()), int)
    # root = iter(inp.split())
    root = build_tree(iter(inp.split()), int)

    # TARGET = 4
    # result = find_target_value(root, TARGET)
    # print(result)
    in_order_traversal(root)
    # pre_order_traversal(root)
