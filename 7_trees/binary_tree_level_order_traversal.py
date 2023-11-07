# LeetCode Link: https://leetcode.com/problems/binary-tree-level-order-traversal/
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        # Initialize the current level with the root node.
        curr_level = [root]
        # Initialize a list to store the levels of the binary tree.
        levels = list()

        while curr_level:
            # Initialize a list for the next level of nodes.
            next_level = list()
            # Initialize a list to store the values of nodes at the current level.
            vals = list()

            # Iterate through nodes at the current level.
            for node in curr_level:
                if node:
                    # Add the left and right child nodes to the next level.
                    next_level.append(node.left)
                    next_level.append(node.right)
                    # Collect the value of the current node.
                    vals.append(node.val)

            # If there are values in the vals list, add them to the levels list.
            if vals:
                levels.append(vals)

            # Move to the next level for the next iteration.
            curr_level = next_level

        # Return the levels list, which contains the level-order traversal.
        return levels
