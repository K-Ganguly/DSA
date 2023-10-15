# Leetcode Link: https://leetcode.com/problems/two-sum/
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        nums_indices = dict()
        for i, num in enumerate(nums):
            num1 = target - num
            if num1 in nums_indices:
                j = nums_indices[num1]
                return [j, i]
            nums_indices[num] = i
