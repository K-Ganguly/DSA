# LeetCode Link: https://leetcode.com/problems/binary-tree-maximum-path-sum/
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        # Initialize the result to the root's value
        res = root.val

        # Helper function to perform depth-first search
        def dfs(root):
            nonlocal res

            # Base case: If the current node is None, return 0
            if not root:
                return 0

            # Calculate the maximum path sum starting from the left and right subtrees
            left_sum = max(0, dfs(root.left))
            right_sum = max(0, dfs(root.right))

            # Calculate the maximum path sum that includes the current node (with_split)
            # and the maximum path sum that doesn't include the current node (without_split)
            with_split = root.val + left_sum + right_sum
            without_split = root.val + max(left_sum, right_sum)

            # Update the global result with the maximum path sum
            res = max(res, with_split)

            # Return the maximum path sum that can be extended upwards to the parent node
            return without_split

        # Start the depth-first search from the root
        dfs(root)

        # Return the maximum path sum found
        return res
