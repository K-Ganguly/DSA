// LeetCode Link: https://leetcode.com/problems/find-the-duplicate-number/
class Solution
{
public:
    int findDuplicate(vector<int> &nums)
    {
        int slow = nums[0], fast = nums[0];

        // Phase 1: Finding the intersection point
        while (true)
        {
            slow = nums[slow];       // Move 'slow' one step at a time.
            fast = nums[nums[fast]]; // Move 'fast' two steps at a time.
            if (slow == fast)        // If 'slow' and 'fast' meet, there's a cycle.
                break;
        }

        // Phase 2: Finding the entry point of the cycle
        slow = nums[0];
        while (slow != fast)
        {
            slow = nums[slow]; // Move 'slow' one step at a time.
            fast = nums[fast]; // Move 'fast' one step at a time.
        }

        return slow; // The entry point of the cycle is the duplicate element.
    }
};
