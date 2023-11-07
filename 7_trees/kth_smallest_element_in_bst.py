# LeetCode Link: https://leetcode.com/problems/kth-smallest-element-in-a-bst/
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


# Approach 1: Iterative (Better approach)
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        # Initialize an empty stack to perform in-order traversal.
        stack = list()
        # Initialize a variable to store the result (kth smallest value).
        res = 0
        # Start traversal from the root node.
        curr = root

        # Continue the traversal while there are nodes to visit or elements in the stack.
        while curr or stack:
            # Traverse as far left as possible and push nodes onto the stack.
            while curr:
                stack.append(curr)
                curr = curr.left

            # Pop the top node from the stack (which is the leftmost unvisited node).
            curr = stack.pop()

            # Decrement k, indicating that we've visited a node.
            k -= 1

            # If k becomes 0, we've found the kth smallest element, so return its value.
            if k == 0:
                return curr.val

            # Move to the right subtree to continue in-order traversal.
            curr = curr.right


# Approach 2: Recursive (Not so good)
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        # Initialize a variable to store the kth smallest value.
        kth_smallest_val = 0

        # Define a recursive in-order traversal function.
        def in_order_traversal(root):
            if not root:
                return None

            nonlocal k  # Declare 'k' as nonlocal to modify it within the function.
            nonlocal kth_smallest_val  # Declare 'kth_smallest_val' as nonlocal to modify it within the function.

            # Traverse the left subtree first.
            in_order_traversal(root.left)

            # Decrement 'k' as we visit each node.
            k -= 1

            # When 'k' becomes 0, we've found the kth smallest element.
            if k == 0:
                kth_smallest_val = root.val
                return

            # Continue to the right subtree.
            in_order_traversal(root.right)

        # Start the in-order traversal from the root node.
        in_order_traversal(root)

        # Return the kth smallest value.
        return kth_smallest_val


"""
Why code 1 is better than code 2??????

- Code 1 (In-Order Recursion): O(h + k) time complexity, where h is the height of the BST. The traversal stops once the kth smallest element is found.

- Code 2 (In-Order Iteration with Stack): O(h + k) time complexity, where h is the height of the BST, and k is the kth smallest element to find. It is also efficient and can stop early when the kth smallest element is found.
Both Code 1 and Code 2 are efficient for finding the kth smallest element, but in practice, Code 2 is often more memory-efficient, especially for large trees, because it doesn't rely on the call stack for recursion.

"""
