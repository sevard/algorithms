#!/usr/bin/env python3


from typing import Optional
from dfs.utils import Node

"""
Max depth of a binary tree is the longest root-to-leaf path. 
Given a binary tree, find its max depth. 

Defined length of the path is the number 
of edges on that path, not the number of nodes.
"""


def get_tree_depth(tree: Optional[Node]) -> int:
    """
    Calculates the maximum depth of a binary tree in terms of edges.
    
    Logic:
    Uses a Depth-First Search (DFS) approach. We first handle the edge case 
    for an empty tree (returning 0). Then, the inner `_dfs` function recursively 
    calculates the maximum number of nodes in a root-to-leaf path. Since depth 
    is defined as the number of edges, we subtract 1 from the total node count 
    at the end.
    
    Time Complexity: 
    O(N) where N is the number of nodes in the tree, because every node 
    is visited exactly once.
    
    Space Complexity: 
    O(H) where H is the maximum height of the tree. This accounts for the 
    recursion call stack. In the worst case (a completely skewed tree), 
    space is O(N). In the best case (a perfectly balanced tree), space is O(log N).
    """

    if tree is None:
        return 0

    def _dfs(node: Optional[Node]) -> int:
        if node is None:
            return 0
        return max(_dfs(node.left), _dfs(node.right)) + 1

    # convert node count to edge count
    return _dfs(tree) - 1
