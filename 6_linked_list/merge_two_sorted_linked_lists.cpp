// LeetCode Link: https://leetcode.com/problems/merge-two-sorted-lists/
/**
 * Definition for singly-linked list->
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
    ListNode *mergeTwoLists(ListNode *list1, ListNode *list2)
    {
        // Create a dummy node to simplify the code.
        ListNode dummy(0);
        // Initialize the pointer to the merged list with the dummy node.
        ListNode *merged_list_curr = &dummy;

        // Loop while both input lists have nodes.
        while (list1 && list2)
        {
            // Compare the values of the current nodes in list1 and list2.
            if (list1->val <= list2->val)
            {
                // Append the node from list1 to the merged list.
                merged_list_curr->next = list1;
                // Move to the next node in list1.
                list1 = list1->next;
            }
            else
            {
                // Append the node from list2 to the merged list.
                merged_list_curr->next = list2;
                // Move to the next node in list2.
                list2 = list2->next;
            }
            // Move the pointer in the merged list to the newly appended node.
            merged_list_curr = merged_list_curr->next;
        }

        // Append any remaining elements from list1 or list2.
        if (list1)
            merged_list_curr->next = list1;
        else
            merged_list_curr->next = list2;

        // Return the merged list starting from the next node of the dummy.
        return dummy.next;
    }
};
