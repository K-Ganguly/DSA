// LeetCode Link: https://leetcode.com/problems/remove-nth-node-from-end-of-list/description/
/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     ListNode *next;
 *     ListNode() : val(0), next(nullptr) {}
 *     ListNode(int x) : val(x), next(nullptr) {}
 *     ListNode(int x, ListNode *next) : val(x), next(next) {}
 * };
 */
class Solution
{
public:
    ListNode *removeNthFromEnd(ListNode *head, int n)
    {
        // Check if the list is empty or has only one node, which would make removal impossible.
        if (!head || !head->next)
            return NULL;

        // Create a dummy node as a temporary head, simplifying the removal process.
        ListNode *temp = new ListNode(0, head);
        ListNode *left = temp;  // Pointer for the node before the one to be removed.
        ListNode *right = head; // Pointer to traverse n nodes ahead of 'left'.

        // Move 'right' n nodes ahead, maintaining a 'n' node gap between 'left' and 'right'.
        while (right && n > 0)
        {
            right = right->next;
            n--;
        }

        // Move both 'left' and 'right' together until 'right' reaches the end of the list.
        while (right)
        {
            left = left->next;
            right = right->next;
        }

        // Update the 'left' node's 'next' pointer to skip the node to be removed.
        left->next = left->next->next;

        // Return the updated list without the removed node.
        return temp->next;
    }
};
