#!/usr/bin/env python3

from typing import Optional
from .utils import Node, build_tree


def in_order_traversal(root: Node) -> None:
    """ Visits the left branch first, then current node,
     and finally the right branch.  <-, self , -> """
    if not root:
        return
    if root.left:
        in_order_traversal(root.left)
    print(root.val)
    if root.right:
        in_order_traversal(root.right)
    return


def pre_order_traversal(root: Node) -> None:
    """ Visits current node first, then left subtree, 
        and finally the right subtree. self, <-, -> """
    if not root:
        return
    print(root.val)
    if root.left:
        pre_order_traversal(root.left)
    if root.right:
        pre_order_traversal(root.right)
    return


def post_order_traversal(root: Node) -> None:
    """ Visits left subtree first, then right subtree,
        and finally current node. <- , ->, self """
    if not root:
        return
    if root.left:
        post_order_traversal(root.left)
    if root.right:
        post_order_traversal(root.right)
    print(root.val)


def dfs(root: Optional[Node], target) -> Optional[int]:
    if root is None:
        return root
    if root.val == target:
        return target

    left = dfs(root.left, target)
    if left is not None:
        return left

    # At this point, we know left is null, and right might or might not be null
    # We return right child's recursive call result directly becasue
    # - if it's non-null, we should return it
    # - if it's null, then both left and right are null, we want to return null
    return dfs(root.right, target)

    # the code can be shortened to: 
    # return dfs(root.left, target) or dfs(root.right, target)


if __name__ == "__main__":
    # inp = "5 4 3 x x 8 x x 6 x x"
    inp = "1 2 3 x 5 x x 4 x x 6 x x"
    # root = build_tree(iter(input().split()), int)
    # root = iter(inp.split())
    root = build_tree(iter(inp.split()), int)

    TARGET = 4
    if root:
        # pre_order_traversal(root)
        result = dfs(root, TARGET)
        print(result)
