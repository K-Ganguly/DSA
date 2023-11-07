# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        # Helper function to build the tree recursively
        def buildTreeHelper(pre_start, pre_end, in_start, in_end):
            # Base case: If the sublist is empty, return None
            if pre_start > pre_end or in_start > in_end:
                return None

            # The first element in the preorder list is the root
            root_val = preorder[pre_start]
            root = TreeNode(root_val)

            # Find the index of the root value in the inorder list
            root_inorder_idx = inorder_index[root_val]

            # Calculate the size of the left subtree
            left_size = root_inorder_idx - in_start

            # Recursively build the left subtree
            left_preorder_start = pre_start + 1
            left_preorder_end = pre_start + left_size
            left_inorder_start = in_start
            left_inorder_end = root_inorder_idx - 1
            root.left = buildTreeHelper(
                left_preorder_start,
                left_preorder_end,
                left_inorder_start,
                left_inorder_end,
            )

            # Recursively build the right subtree
            right_preorder_start = pre_start + left_size + 1
            right_preorder_end = pre_end
            right_inorder_start = root_inorder_idx + 1
            right_inorder_end = in_end
            root.right = buildTreeHelper(
                right_preorder_start,
                right_preorder_end,
                right_inorder_start,
                right_inorder_end,
            )

            return root

        # Create a dictionary to store indices of elements in the inorder list for efficient lookup
        inorder_index = {val: idx for idx, val in enumerate(inorder)}

        # Start building the tree with the entire preorder and inorder lists
        return buildTreeHelper(0, len(preorder) - 1, 0, len(inorder) - 1)
