#!/usr/bin/env python3

from typing import Optional, Iterator, Callable


class Node:
    def __init__(self, val: int, left=None, right=None) -> None:
        self.val = val
        self.left = left
        self.right = right


# learn more about how trees are encoded in https://algo.monster/problems/serializing_tree
def build_tree(nodes: Iterator[str], func: Callable[[str], int]) -> Optional[Node]:
    try:
        val = next(nodes)
    except StopIteration:
        val = None

    if val == "x" or val is None:
        return None

    left = build_tree(nodes, func)
    right = build_tree(nodes, func)
    return Node(func(val), left, right)


def print_tree(node, prefix="", is_left=True, is_root=True):

    if node is None:
        return

    if node.right:
        new_prefix = prefix + ("│  " if is_left and not is_root else "   ")
        print_tree(node.right, new_prefix, is_left=False, is_root=False)

    if is_root:
        print(f"{node.val} ─│")
    else:
        print(f"{prefix}{'└─' if is_left else '┌─'}{node.val}")

    if node.left:
        new_prefix = prefix + ("│  " if not is_left and not is_root else "   ")
        print_tree(node.left, new_prefix, is_left=True, is_root=False)


def pretty_print_tree(node):
    """
    Pretty prints a binary tree in a beautiful top-down horizontal layout.
    """
    if node is None:
        print("(empty tree)")
        return

    def _build_layout(curr):
        if curr is None:
            return [], 0, 0, 0

        label = str(curr.val)

        left_lines, left_w, left_h, left_r = _build_layout(curr.left)
        right_lines, right_w, right_h, right_r = _build_layout(curr.right)

        if not left_lines and not right_lines:
            return [label], len(label), 1, len(label) // 2

        parent_root = len(label) // 2

        if not left_lines:
            shift = max(len(label), parent_root + 2 - right_r)
            new_width = shift + right_w

            lines = [label.ljust(new_width)]
            conn = ' ' * parent_root + '└' + '─' * \
                (shift + right_r - parent_root - 1) + '┐'
            lines.append(conn.ljust(new_width))

            for line in right_lines:
                lines.append((' ' * shift + line).ljust(new_width))

            return lines, new_width, len(lines), parent_root

        if not right_lines:
            shift = max(left_w, left_r + 2 - parent_root)
            new_width = shift + len(label)

            lines = [(' ' * shift + label).ljust(new_width)]
            conn = ' ' * left_r + '┌' + '─' * \
                (shift + parent_root - left_r - 1) + '┘'
            lines.append(conn.ljust(new_width))

            for line in left_lines:
                lines.append(line.ljust(new_width))

            return lines, new_width, len(lines), shift + parent_root

        arm = max(1, left_w + parent_root - left_r - 1,
                  right_r - parent_root + len(label) - 1)
        new_root = left_r + arm + 1
        shift = new_root + arm + 1 - right_r
        new_width = shift + right_w

        lines = []
        parent_start = new_root - parent_root
        lines.append((' ' * parent_start + label).ljust(new_width))

        conn = ' ' * left_r + '┌' + '─' * arm + '┴' + '─' * arm + '┐'
        lines.append(conn.ljust(new_width))

        left_h = len(left_lines)
        right_h = len(right_lines)
        for i in range(max(left_h, right_h)):
            left_part = left_lines[i] if i < left_h else ""
            right_part = right_lines[i] if i < right_h else ""
            merged_line = left_part.ljust(shift) + right_part
            lines.append(merged_line.ljust(new_width))

        return lines, new_width, len(lines), new_root

    tree_lines, _, _, _ = _build_layout(node)
    for line in tree_lines:
        print(line.rstrip())
