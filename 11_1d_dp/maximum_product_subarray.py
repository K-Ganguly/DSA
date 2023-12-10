# LeetCode Link: https://leetcode.com/problems/maximum-product-subarray/
class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        # Initialize variables to keep track of prefix, suffix, and maximum subarray product
        prefix = 1
        suffix = 1
        max_subarr_prd = float("-inf")

        # Get the length of the input array
        n = len(nums)

        # Iterate through the array
        for i in range(n):
            # Update prefix and suffix products
            prefix *= nums[i]
            suffix *= nums[n - i - 1]

            # Update the maximum subarray product by considering the current prefix, suffix, and the previous maximum
            max_subarr_prd = max(prefix, suffix, max_subarr_prd)

            # If prefix becomes 0, reset it to 1
            if prefix == 0:
                prefix = 1

            # If suffix becomes 0, reset it to 1
            if suffix == 0:
                suffix = 1

        # Return the maximum subarray product
        return max_subarr_prd
