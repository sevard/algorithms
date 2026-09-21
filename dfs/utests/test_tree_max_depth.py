from dfs.utils import Node, build_tree
from dfs.tree_max_depth import get_tree_depth


def test_empty_tree():
    """Test max depth of an empty tree."""
    assert get_tree_depth(None) == 0


def test_single_node():
    """Test max depth of a tree with only a root node."""
    node = Node(1)
    assert get_tree_depth(node) == 0


def test_tree_with_two_nodes():
    """Test max depth of a tree with a root and one child."""
    node = Node(1, left=Node(2))
    assert get_tree_depth(node) == 1


def test_balanced_tree():
    """Test max depth of a perfectly balanced tree."""
    #      1
    #     / \
    #    2   3
    #   / \ / \
    #  4  5 6  7
    nodes = iter(["1", "2", "4", "x", "x", "5", "x",
                 "x", "3", "6", "x", "x", "7", "x", "x"])
    tree = build_tree(nodes, int)
    assert get_tree_depth(tree) == 2


def test_right_skewed_tree():
    """Test max depth of a completely right-skewed tree."""
    # 1
    #  \
    #   2
    #    \
    #     3
    #      \
    #       4
    nodes = iter(["1", "x", "2", "x", "3", "x", "4", "x", "x"])
    tree = build_tree(nodes, int)
    assert get_tree_depth(tree) == 3


def test_left_skewed_tree():
    """Test max depth of a completely left-skewed tree."""
    #     1
    #    /
    #   2
    #  /
    # 3
    nodes = iter(["1", "2", "3", "x", "x", "x", "x"])
    tree = build_tree(nodes, int)
    assert get_tree_depth(tree) == 2


def test_complex_unbalanced_tree():
    """Test max depth of a complex, unevenly structured tree."""
    #      1
    #     / \
    #    2   3
    #   /     \
    #  4       5
    #   \
    #    6
    nodes = iter(["1", "2", "4", "x", "6", "x",
                 "x", "x", "3", "x", "5", "x", "x"])
    tree = build_tree(nodes, int)
    assert get_tree_depth(tree) == 3
