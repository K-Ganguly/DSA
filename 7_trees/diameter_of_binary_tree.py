# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        diameter = 0  # Initialize a variable to store the diameter of the binary tree.

        def findDepth(root):
            nonlocal diameter  # Declare that we are using the 'diameter' variable from the outer function.

            if not root:
                return 0  # If the current node is None, return a depth of 0.

            left_depth = findDepth(
                root.left
            )  # Recursively find the depth of the left subtree.
            right_depth = findDepth(
                root.right
            )  # Recursively find the depth of the right subtree.

            # Calculate the diameter of the binary tree using the current node as a potential
            # part of the diameter. It is the maximum of the current 'diameter' value and
            # the sum of depths of left and right subtrees.
            diameter = max(diameter, (left_depth + right_depth))

            # Return the maximum depth of the left and right subtrees, plus 1 to account for the current node.
            return max(left_depth, right_depth) + 1

        depth = findDepth(
            root
        )  # Call the helper function to find the depth of the binary tree rooted at 'root'.
        return diameter  # Return the calculated diameter of the binary tree.
