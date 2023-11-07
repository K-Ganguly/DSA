# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        is_balanced = True  # Initialize a variable to store whether the binary tree is balanced or not.

        def findDepth(root):
            nonlocal is_balanced  # Declare that we are using the 'is_balanced' variable from the outer function.
            if not root:
                return 0  # If the current node is None, return a depth of 0.

            left_depth = findDepth(
                root.left
            )  # Recursively find the depth of the left subtree.
            right_depth = findDepth(
                root.right
            )  # Recursively find the depth of the right subtree.

            # Check if the absolute difference between the depths of the left and right subtrees is greater than 1.
            # If it is, the tree is not balanced, and we set 'is_balanced' to False.
            if abs(left_depth - right_depth) > 1:
                is_balanced = False

            # Return the maximum depth of the left and right subtrees, plus 1 to account for the current node.
            return max(left_depth, right_depth) + 1

        depth = findDepth(
            root
        )  # Call the helper function to find the depth of the binary tree rooted at 'root'.

        return is_balanced  # Return the boolean value indicating whether the binary tree is balanced or not.
