# LeetCode Link: https://leetcode.com/problems/binary-tree-right-side-view/
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

from collections import deque


class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        # Initialize an empty list to store the right side view of the binary tree.
        view = list()

        # Initialize a deque with the root node for level-order traversal.
        level = deque([root])

        while level:
            right_side = None  # Initialize a variable to store the rightmost node at the current level.
            level_len = len(level)  # Get the number of nodes at the current level.

            for _ in range(level_len):
                node = level.popleft()  # Get the next node from the queue.

                if node:
                    # Add the left and right child nodes to the queue.
                    level.append(node.left)
                    level.append(node.right)

                    right_side = node  # Update the rightmost node at the current level.

            if right_side:
                view.append(
                    right_side.val
                )  # Add the value of the rightmost node to the view.

        return view
