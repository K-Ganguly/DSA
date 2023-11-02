// LeetCode Link: https://leetcode.com/problems/reorder-list/
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
    void reorderList(ListNode *head)
    {
        // Check if the list is empty or has only one node, no reordering needed.
        if (!head || !head->next)
            return;

        // Step 1: Find the middle of the list using slow and fast pointers.
        ListNode *slow = head, *fast = head;
        while (fast && fast->next)
        {
            slow = slow->next;       // Slow pointer advances by one step.
            fast = fast->next->next; // Fast pointer advances by two steps.
        }

        // Step 2: Reverse the second half of the list.
        ListNode *prev = nullptr;
        ListNode *curr = slow;
        while (curr)
        {
            ListNode *temp = curr->next;
            curr->next = prev; // Reverse the next pointer of the current node.
            prev = curr;       // Move the prev pointer to the current node.
            curr = temp;       // Move the current pointer to the next node.
        }

        // Step 3: Merge the two halves of the list.
        ListNode *curr1 = head;
        ListNode *curr2 = prev; // curr2 now points to the reversed second half.
        while (curr2->next)
        {
            ListNode *temp1 = curr1->next;
            ListNode *temp2 = curr2->next;
            curr1->next = curr2; // Merge the first half node with the reversed second half node.
            curr2->next = temp1; // Connect the reversed second half node to the first half.
            curr1 = temp1;       // Move the first half pointer to its next node.
            curr2 = temp2;       // Move the reversed second half pointer to its next node.
        }
    }
};
