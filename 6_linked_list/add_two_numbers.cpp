class Solution
{
public:
    ListNode *addTwoNumbers(ListNode *l1, ListNode *l2)
    {
        ListNode *digit1 = l1;
        ListNode *digit2 = l2;
        ListNode *head_s = nullptr;
        ListNode *curr_s = nullptr;
        int carry = 0;

        while (digit1 || digit2 || carry)
        {
            // Get the values of the current digits or set them to 0 if the node is null.
            int val1, val2;
            if (digit1)
            {
                val1 = digit1->val;
                digit1 = digit1->next;
            }
            else
            {
                val1 = 0;
            }

            if (digit2)
            {
                val2 = digit2->val;
                digit2 = digit2->next;
            }
            else
            {
                val2 = 0;
            }

            // Calculate the sum of the current digits and any carry from the previous iteration.
            int sum_val = val1 + val2 + carry;
            int sum_digit = sum_val % 10;
            carry = sum_val / 10;

            // Create a new ListNode for the sum_digit.
            ListNode *sum = new ListNode(sum_digit);

            // Update the result list.
            if (!head_s)
            {
                curr_s = sum;
                head_s = curr_s;
            }
            else
            {
                curr_s->next = sum;
                curr_s = curr_s->next;
            }
        }

        // Return the head of the result list.
        return head_s;
    }
};
