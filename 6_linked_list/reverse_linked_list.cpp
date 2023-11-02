// LeetCode Link: https://leetcode.com/problems/reverse-linked-list/

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
    ListNode *reverseList(ListNode *head)
    {
        // Initialize two pointers, 'prev' and 'curr', and set 'prev' to NULL.
        ListNode *prev = NULL;
        ListNode *curr = head;

        // While 'curr' is not NULL (while there are nodes in the original list):
        while (curr)
        {
            // Store the next node in the original list in 'temp'.
            ListNode *temp = curr->next;

            // Reverse the 'next' pointer of 'curr' to point to 'prev'.
            curr->next = prev;

            // Move 'prev' and 'curr' one step forward.
            prev = curr;
            curr = temp;
        }

        // 'prev' now points to the new head of the reversed list, so return it.
        return prev;
    }
};
