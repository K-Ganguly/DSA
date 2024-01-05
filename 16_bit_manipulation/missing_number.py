# https://leetcode.com/problems/missing-number/
class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        # Determine the length of the array
        n = len(nums)

        # Initialize a variable to store the missing number
        missing_num = 0

        # XOR all numbers from 0 to n (inclusive)
        for num in range(n + 1):
            missing_num ^= num

        # XOR all numbers in the given array
        for num in nums:
            missing_num ^= num

        # The final value of missing_num is the missing number in the array
        return missing_num
