from dfs.utils import Node, build_tree
from dfs.visible_tree_node import count_visible_nodes_v1, count_visible_nodes_v2


def test_empty_tree():
    """Test visible count for an empty tree."""
    assert count_visible_nodes_v1(None) == 0
    assert count_visible_nodes_v2(None) == 0


def test_single_node():
    """Test visible count for a tree with only a root node."""
    node = Node(7)
    assert count_visible_nodes_v1(node) == 1
    assert count_visible_nodes_v2(node) == 1


def test_root_only_visible():
    """Test a tree where only the root remains visible."""
    #      3
    #     / \
    #    2   1
    nodes = iter(["3", "2", "x", "x", "1", "x", "x"])
    tree = build_tree(nodes, int)
    assert count_visible_nodes_v1(tree) == 1
    assert count_visible_nodes_v2(tree) == 1


def test_deep_right_branch_increases_visibility():
    """Test a tree where a deeper right-side node is visible."""
    #      -100
    #          \
    #          -500
    #               \
    #               -50
    nodes = iter(["-100", "x", "-500", "x", "-50", "x", "x"])
    tree = build_tree(nodes, int)
    assert count_visible_nodes_v1(tree) == 2
    assert count_visible_nodes_v2(tree) == 2


def test_multiple_visible_nodes_across_branches():
    """Test a tree with several visible nodes across both sides."""
    #      5
    #     / \
    #    4   6
    #   / \
    #  3   8
    nodes = iter(["5", "4", "3", "x", "x", "8", "x", "x", "6", "x", "x"])
    tree = build_tree(nodes, int)
    assert count_visible_nodes_v1(tree) == 3
    assert count_visible_nodes_v2(tree) == 3
