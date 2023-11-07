# LeetCode Link: https://leetcode.com/problems/validate-binary-search-tree/
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        # Define a recursive function to check the validity of a binary search tree.
        def checkValid(root, max_left, min_right):
            # Base case: If the current node is None, it's a valid BST.
            if not root:
                return True

            # Check if the current node's value is within the valid range defined by its ancestors.
            if not (max_left < root.val < min_right):
                return False

            # Recursively check the left and right subtrees, updating the valid range accordingly.
            # For the left subtree, the maximum value (max_left) is updated to the current node's value,
            # and for the right subtree, the minimum value (min_right) is updated to the current node's value.
            return checkValid(root.left, max_left, root.val) and checkValid(
                root.right, root.val, min_right
            )

        # Start the validation process from the root node with an initial valid range of negative infinity to positive infinity.
        return checkValid(root, float("-inf"), float("inf"))
