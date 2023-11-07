# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        # If both nodes are None, they are the same (base case).
        if not p and not q:
            return True

        # If one of the nodes is None but the other is not, they are different (base case).
        if not p or not q:
            return False

        # If neither node is None, compare their values.
        # If values are equal, recursively check their left and right subtrees.
        return (
            (p.val == q.val)
            and self.isSameTree(p.left, q.left)
            and self.isSameTree(p.right, q.right)
        )
