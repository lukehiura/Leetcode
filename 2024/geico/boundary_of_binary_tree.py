# Problem 545. Boundary of Binary Tree
# Difficulty: Medium
#
# The boundary of a binary tree is the concatenation of the root, the left boundary, the leaves ordered from left-to-right,
#  and the reverse order of the right boundary.

# The left boundary is the set of nodes defined by the following:

# The root node's left child is in the left boundary. If the root does not have a left child, then the left boundary is empty.
# If a node in the left boundary and has a left child, then the left child is in the left boundary.
# If a node is in the left boundary, has no left child, but has a right child, then the right child is in the left boundary.
# The leftmost leaf is not in the left boundary.
# The right boundary is similar to the left boundary, except it is the right side of the root's right subtree. 
# Again, the leaf is not part of the right boundary, and the right boundary is empty if the root does not have a right child.

# The leaves are nodes that do not have any children. For this problem, the root is not a leaf.

# Given the root of a binary tree, return the values of its boundary.
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

# root -> 


from typing import List, Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def boundaryOfBinaryTree(root: Optional[TreeNode]) -> List[int]:
    if not root:
        return []
    
    ans = [root.val]

    # Helper function to add left boundary nodes, excluding leaves
    def left_boundary(node) -> None:
        while node:
            if node.left or node.right:  # Exclude leaf nodes
                ans.append(node.val)
            if node.left:
                node = node.left
            else:
                node = node.right

    # Helper function to add leaf nodes only
    def leaves(node) -> None:
        if node:
            if not node.left and not node.right:  # Leaf node
                ans.append(node.val)
            leaves(node.left)
            leaves(node.right)

    # Helper function to add right boundary nodes in reverse order, excluding leaves
    def right_boundary(node) -> None:
        stack = []
        while node:
            if node.left or node.right:  # Exclude leaf nodes
                stack.append(node.val)
            if node.right:
                node = node.right
            else:
                node = node.left
        while stack:
            ans.append(stack.pop())  # Add in reverse order

    # Collect the boundary values in the correct order
    if root.left:
        left_boundary(root.left)
    leaves(root.left)
    leaves(root.right)
    if root.right:
        right_boundary(root.right)

    return ans

# Helper function to build a binary tree from list input (for testing)
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

# Test Case 5 - Complete binary tree
root5 = build_tree_from_list([1, 2, 3, 4, 5, 6, 7])
assert boundaryOfBinaryTree(root5) == [1, 2, 4, 5, 6, 7, 3], f"Test Case 6 Failed: {boundaryOfBinaryTree(root5)} != [1, 2, 4, 5, 6, 7, 3]"

print("All test cases passed!")
