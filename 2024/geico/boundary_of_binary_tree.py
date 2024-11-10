# Problem 545. Boundary of Binary Tree
# Difficulty: Medium
#
# Description:
# The boundary of a binary tree is the concatenation of:
#   - The root,
#   - The left boundary (excluding the leftmost leaf),
#   - The leaves (ordered from left-to-right),
#   - The right boundary (in reverse order, excluding the rightmost leaf).
#
# Definitions:
# - Left boundary:
#     - Includes the root's left child if it exists.
#     - If a node has a left child, the left child is in the left boundary.
#     - If a node has no left child but has a right child, the right child is in the left boundary.
#     - The leftmost leaf is excluded from the left boundary.
# - Right boundary:
#     - Similar to the left boundary, but on the right side of the root's right subtree.
#     - The right boundary is empty if the root does not have a right child.
# - Leaves:
#     - Nodes without children (not including the root).
#
# Input: The root of a binary tree.
# Output: A list of integers representing the boundary values in order.
#
# Example 1:
# Input: root = [1, None, 2, 3, 4]
# Output: [1, 3, 4, 2]
# Explanation:
# - Left boundary is empty (no left child for the root).
# - Right boundary is [2].
# - Leaves are [3,4].
# - Concatenated result: [1] + [] + [3,4] + [2] = [1, 3, 4, 2].
#
# Example 2:
# Input: root = [1, 2, 3, 4, 5, 6, None, None, None, 7, 8, 9, 10]
# Output: [1, 2, 4, 7, 8, 9, 10, 6, 3]
# Explanation:
# - Left boundary is [2, 4].
# - Right boundary in reverse order is [6, 3].
# - Leaves are [4, 7, 8, 9, 10].
# - Concatenated result: [1] + [2, 4] + [4, 7, 8, 9, 10] + [6, 3] = [1, 2, 4, 7, 8, 9, 10, 6, 3].
#
# Constraints:
# - The number of nodes in the tree is in the range [1, 10^4].
# - Node values are in the range [-1000, 1000].

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

from typing import List, Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def boundaryOfBinaryTree(root: Optional[TreeNode]) -> List[int]:
    pass






















# Helper function

def build_tree_from_list(values):
    if not values:
        return None
    root = TreeNode(values[0])
    queue = [root]
    i = 1
    while i < len(values):
        node = queue.pop(0)
        if values[i] is not None:
            node.left = TreeNode(values[i])
            queue.append(node.left)
        i += 1
        if i < len(values) and values[i] is not None:
            node.right = TreeNode(values[i])
            queue.append(node.right)
        i += 1
    return root

# Test Cases

# Test Case 1
root1 = build_tree_from_list([1, None, 2, 3, 4])
assert boundaryOfBinaryTree(root1) == [1, 3, 4, 2], f"Test Case 1 Failed: {boundaryOfBinaryTree(root1)} != [1, 3, 4, 2]"

# Test Case 2
root2 = build_tree_from_list([1, 2, 3, 4, 5, 6, None, None, None, 7, 8, 9, 10])
assert boundaryOfBinaryTree(root2) == [1, 2, 4, 7, 8, 9, 10, 6, 3], f"Test Case 2 Failed: {boundaryOfBinaryTree(root2)} != [1, 2, 4, 7, 8, 9, 10, 6, 3]"

# Additional Test Cases
# Test Case 3 - Edge case with single node
root3 = build_tree_from_list([1])
assert boundaryOfBinaryTree(root3) == [1], f"Test Case 3 Failed: {boundaryOfBinaryTree(root3)} != [1]"

# Test Case 4 - Left-skewed tree
root4 = build_tree_from_list([1, 2, None, 3, None, 4, None])
assert boundaryOfBinaryTree(root4) == [1, 2, 3, 4], f"Test Case 4 Failed: {boundaryOfBinaryTree(root4)} != [1, 2, 3, 4]"

# Test Case 5 - Right-skewed tree
root5 = build_tree_from_list([1, None, 2, None, 3, None, 4])
assert boundaryOfBinaryTree(root5) == [1, 2, 3, 4], f"Test Case 5 Failed: {boundaryOfBinaryTree(root5)} != [1, 2, 3, 4]"

# Test Case 6 - Complete binary tree
root6 = build_tree_from_list([1, 2, 3, 4, 5, 6, 7])
assert boundaryOfBinaryTree(root6) == [1, 2, 4, 5, 6, 7, 3], f"Test Case 6 Failed: {boundaryOfBinaryTree(root6)} != [1, 2, 4, 5, 6, 7, 3]"

print("All test cases passed!")