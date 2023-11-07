# LeetCode Link: https://leetcode.com/problems/count-good-nodes-in-binary-tree/
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        # Initialize a variable to count the number of "good" nodes.
        num_good_nodes = 0
        # Initialize a variable to keep track of the maximum value encountered in the path.
        max_val_node = float("-inf")

        # Define a recursive function to traverse the tree and count good nodes.
        def traverse(root, max_val_node):
            nonlocal num_good_nodes  # Declare 'num_good_nodes' as nonlocal to modify it within the function.
            if not root:
                return None  # Base case: If the node is None, return.

            if root.val >= max_val_node:
                # If the current node's value is greater than or equal to the maximum value
                # encountered in the path, it's a "good" node, so we increment the count.
                num_good_nodes += 1
                max_val_node = root.val  # Update the maximum value encountered.

            # Recursively traverse the left and right subtrees with the updated max_val_node.
            traverse(root.left, max_val_node)
            traverse(root.right, max_val_node)

        # Start the traversal from the root node with an initial max_val_node of negative infinity.
        traverse(root, max_val_node)

        # Return the count of "good" nodes.
        return num_good_nodes
