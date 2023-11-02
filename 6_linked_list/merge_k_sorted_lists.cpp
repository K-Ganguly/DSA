// LeetCode Link: https://leetcode.com/problems/merge-k-sorted-lists/description/
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
private:
    ListNode *merge2Lists(ListNode *curr1, ListNode *curr2)
    {
        if (!curr1)
            return curr2;
        if (!curr2)
            return curr1;
        ListNode *dummy = new ListNode(0);
        ListNode *merged = dummy;
        while (curr1 && curr2)
        {
            if (curr1->val <= curr2->val)
            {
                merged->next = curr1;
                curr1 = curr1->next;
            }
            else
            {
                merged->next = curr2;
                curr2 = curr2->next;
            }
            merged = merged->next;
        }
        if (curr1)
            merged->next = curr1;
        else
            merged->next = curr2;
        return dummy->next;
    }

public:
    ListNode *mergeKLists(vector<ListNode *> &lists)
    {
        deque<ListNode *> merged_lists(lists.begin(), lists.end());
        while (merged_lists.size() > 1)
        {
            ListNode *l1 = merged_lists.front();
            merged_lists.pop_front();
            ListNode *l2 = merged_lists.front();
            merged_lists.pop_front();
            ListNode *merged_list = merge2Lists(l1, l2);
            merged_lists.push_back(merged_list);
        }
        if (merged_lists.empty())
        {
            return nullptr;
        }

        return merged_lists[0];
    }
}; /**
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
private:
    // Merge two sorted linked lists and return the merged list.
    ListNode *merge2Lists(ListNode *curr1, ListNode *curr2)
    {
        // Check if either of the lists is empty and return the other list as it is.
        if (!curr1)
            return curr2;
        if (!curr2)
            return curr1;

        // Create a dummy node to simplify the merging process.
        ListNode *dummy = new ListNode(0);
        ListNode *merged = dummy;

        // Merge the two lists by comparing node values.
        while (curr1 && curr2)
        {
            if (curr1->val <= curr2->val)
            {
                merged->next = curr1;
                curr1 = curr1->next;
            }
            else
            {
                merged->next = curr2;
                curr2 = curr2->next;
            }
            merged = merged->next;
        }

        // Attach any remaining nodes from either list to the merged list.
        if (curr1)
            merged->next = curr1;
        else
            merged->next = curr2;

        return dummy->next; // Return the merged list starting from the next node of the dummy.
    }

public:
    // Merge k sorted lists using a divide and conquer approach.
    ListNode *mergeKLists(vector<ListNode *> &lists)
    {
        deque<ListNode *> merged_lists(lists.begin(), lists.end()); // Create a deque of the input lists.

        // Continue merging pairs of lists until there's only one list left in the deque.
        while (merged_lists.size() > 1)
        {
            ListNode *l1 = merged_lists.front();
            merged_lists.pop_front();
            ListNode *l2 = merged_lists.front();
            merged_lists.pop_front();

            // Merge the two lists and add the merged list back to the deque.
            ListNode *merged_list = merge2Lists(l1, l2);
            merged_lists.push_back(merged_list);
        }

        if (merged_lists.empty())
        {
            return nullptr; // No lists to merge, return nullptr.
        }

        return merged_lists[0]; // Return the final merged list.
    }
};
