# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next


class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        # Helper function to get the k-th node from the current node
        def getKthNode(curr, k):
            while curr and k > 0:
                curr = curr.next
                k -= 1
            return curr

        # Create a dummy node to simplify handling edge cases
        dummy = ListNode()
        dummy.next = head
        group_prev = dummy  # Initialize the group's previous node as the dummy node

        while True:
            kth_node = getKthNode(
                group_prev, k
            )  # Get the k-th node from the current group_prev
            if not kth_node:
                break  # If there are fewer than k nodes left, we cannot reverse them, so break the loop

            # Reversing the group of k nodes
            group_next = kth_node.next  # Store the next node after the k nodes
            prev = (
                group_next  # Initialize the previous node as the node after the k nodes
            )
            curr = group_prev.next  # Start reversing from the first node in the group
            while curr != group_next:
                temp = curr.next
                curr.next = prev
                prev = curr
                curr = temp

            temp = group_prev.next  # Store the first node of the reversed group
            group_prev.next = kth_node  # Update the group's previous node to the last node of the reversed group
            group_prev = temp  # Move the group_prev to the first node of the reversed group for the next iteration

        return dummy.next  # Return the updated list after reversing groups of k nodes
