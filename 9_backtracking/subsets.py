# LeetCode Link: https://leetcode.com/problems/subsets/


class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        # Base case: if the input list is empty, return a list containing an empty list
        if len(nums) == 0:
            return [[]]

        # Choose the first element from the list
        first_element = nums[0]

        # Recursively get all subsets without the first element
        subsets_without_first = self.subsets(nums[1:])

        # Generate subsets that include the first element by appending it to each subset without the first element
        subsets_with_first = [
            [first_element] + subset for subset in subsets_without_first
        ]

        # Combine subsets with the first element and subsets without the first element
        return subsets_with_first + subsets_without_first
