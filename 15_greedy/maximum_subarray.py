# LeetCode Link: https://leetcode.com/problems/maximum-subarray/
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        # Initialize the sum of the current subarray to 0
        sum_till_curr = 0

        # Initialize the maximum sum of any subarray ending at the current position
        max_sum_till_curr = nums[0]

        # Iterate through each element in the array
        for num in nums:
            # Add the current element to the current subarray sum
            sum_till_curr += num

            # Update the maximum sum of any subarray ending at the current position
            max_sum_till_curr = max(max_sum_till_curr, sum_till_curr)

            # If the current subarray sum becomes negative, reset it to 0
            if sum_till_curr < 0:
                sum_till_curr = 0

        # Return the maximum sum of any subarray found
        return max_sum_till_curr
