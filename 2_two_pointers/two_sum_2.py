# Leetcode Link: https://leetcode.com/problems/two-sum-ii-input-array-is-sorted/
class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        i = 0
        j = len(numbers) - 1
        while i < j:
            number_sum = numbers[i] + numbers[j]
            if number_sum == target:
                return [(i + 1), (j + 1)]
            elif number_sum < target:
                i += 1
            else:
                j -= 1
