// LeetCode Link: https://leetcode.com/problems/linked-list-cycle/
/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     ListNode *next;
 *     ListNode(int x) : val(x), next(NULL) {}
 * };
 */
class Solution
{
public:
    bool hasCycle(ListNode *head)
    {
        // Check if the list is empty or has only one node, in which case a cycle is impossible.
        if (!head || !head->next)
            return false;

        // Initialize two pointers, 'slow' and 'fast,' to traverse the list.
        ListNode *slow = head;
        ListNode *fast = head;

        // Traverse the list with 'fast' moving twice as fast as 'slow.'
        while (fast && fast->next)
        {
            slow = slow->next;       // Move 'slow' by one step.
            fast = fast->next->next; // Move 'fast' by two steps.

            // If there is a cycle, 'slow' and 'fast' will eventually meet at the same node.
            if (slow == fast)
                return true;
        }

        // If 'fast' reaches the end of the list (or 'fast->next' does), there is no cycle.
        return false;
    }
};
