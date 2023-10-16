# LeetCode Link: https://leetcode.com/problems/two-sum/
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # Create a dictionary to store the indices of numbers encountered.
        nums_indices = dict()

        for i, num in enumerate(nums):
            # Calculate the complement of the current number with respect to the target.
            num1 = target - num

            # Check if the complement (num1) is found in the dictionary.
            if num1 in nums_indices:
                # If found, return the indices of the two numbers that add up to the target.
                j = nums_indices[num1]
                return [j, i]

            # Store the current number and its index in the dictionary.
            nums_indices[num] = i
