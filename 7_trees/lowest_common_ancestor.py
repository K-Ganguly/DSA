# LeetCode Link: https://leetcode.com/problems/lowest-common-ancestor-of-a-binary-search-tree/
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution:
    def lowestCommonAncestor(
        self, root: "TreeNode", p: "TreeNode", q: "TreeNode"
    ) -> "TreeNode":
        # Start from the root of the binary search tree.
        curr = root
        while True:
            # If both p and q are less than the current node's value,
            # it means the lowest common ancestor must be on the left subtree.
            if p.val < curr.val and q.val < curr.val:
                curr = curr.left
            # If both p and q are greater than the current node's value,
            # it means the lowest common ancestor must be on the right subtree.
            elif p.val > curr.val and q.val > curr.val:
                curr = curr.right
            # If one of the nodes is less than the current node's value
            # and the other is greater, it means the current node is the lowest
            # common ancestor, as it is the first node where the paths of p and q diverge.
            else:
                return curr
