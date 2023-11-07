# LeetCode Link: https://leetcode.com/problems/invert-binary-tree/
class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        # Check if the root node exists
        if root:
            # Swap the left and right children of the current node
            root.left, root.right = root.right, root.left
            # Recursively invert the left subtree
            self.invertTree(root.left)
            # Recursively invert the right subtree
            self.invertTree(root.right)
        # Return the modified root node (or None if it's the base case)
        return root
