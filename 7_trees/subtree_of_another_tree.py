# LeetCode Link: https://leetcode.com/problems/subtree-of-another-tree/
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


class Solution:
    def isSametree(self, root1, root2):
        # Check if both trees are empty (base case).
        if not (root1) and not (root2):
            return True
        # Check if one of the trees is empty, but not both.
        if not (root1) or not (root2):
            return False
        # Check if the current nodes have the same value and recursively
        # check the left and right subtrees.
        if root1.val == root2.val:
            return self.isSametree(root1.left, root2.left) and self.isSametree(
                root1.right, root2.right
            )
        # If the values of the current nodes are not the same, the trees are not the same.
        return False

    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        # Check if the subtree is empty, which is always a valid subtree.
        if not (subRoot):
            return True
        # If the main tree is empty, it cannot contain a subtree.
        if not (root):
            return False
        # Check if the current root of the main tree matches the subtree.
        # If it doesn't match, recursively check the left and right subtrees of the main tree.
        return (
            self.isSametree(root, subRoot)
            or self.isSubtree(root.left, subRoot)
            or self.isSubtree(root.right, subRoot)
        )
