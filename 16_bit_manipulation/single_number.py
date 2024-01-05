# LeetCode Link: https://leetcode.com/problems/single-number/
class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        # Initialize the result variable to 0
        res = 0

        # Iterate through the given list of numbers
        for num in nums:
            # Use bitwise XOR operation (^) on each number
            # XOR of a number with itself is 0, and XOR of any number with 0 is the number itself
            # So, the result will eventually be the single number that appears only once
            res ^= num

        # Return the final result
        return res
