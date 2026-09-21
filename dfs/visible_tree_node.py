#!/usr/bin/env python3

from math import inf
from typing import Optional
from dfs.utils import Node, build_tree


"""
Explanation: 
    In a binary tree, a node is labled as 'visible' if, 
    on the path from the root to that node, there isn't 
    any node with a value higher that this node's value

Problem: 
    Given a binary tree, 
    find the number of nodes that are 'visible'
"""


def _dfs(node: Optional[Node], max_sofar: int) -> int:
    if not node:
        return 0
    total_visible_nodes = 0
    if node.val >= max_sofar:
        total_visible_nodes += 1

    total_visible_nodes += _dfs(node.left, max(node.val, max_sofar))
    total_visible_nodes += _dfs(node.right, max(node.val, max_sofar))
    return total_visible_nodes


def count_visible_nodes_v1(root: Optional[Node]) -> int:
    if not root:
        return 0
    return _dfs(root, root.val - 1)


def count_visible_nodes_v2(node: Optional[Node], max_sofar=-inf) -> int:
    """ Version with no auxilary dfs function"""
    total = 0
    if not node:
        return 0
    if node.val >= max_sofar:
        total += 1
    total += count_visible_nodes_v2(node.left, max(node.val, max_sofar))
    total += count_visible_nodes_v2(node.right, max(node.val, max_sofar))
    return total


if __name__ == "__main__":
    node_1 = build_tree(iter("3 2 x x 1 x x".split()), int)
    node_3 = build_tree(iter("5 4 3 x x 8 x x 6 x x".split()), int)
    node_2 = build_tree(iter("-100 x -500 x -50 x x".split()), int)

    assert count_visible_nodes_v1(node_1) == 1 
    assert count_visible_nodes_v1(node_2) == 2
    assert count_visible_nodes_v1(node_3) == 3
    #
    assert count_visible_nodes_v2(node_1) == 1
    assert count_visible_nodes_v2(node_2) == 2
    assert count_visible_nodes_v2(node_3) == 3
