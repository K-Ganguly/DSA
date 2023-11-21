# LeetCode Link: https://leetcode.com/problems/permutations/
class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        perms = []

        # Recursive function to generate permutations starting from a specific index
        def get_permutation(start):
            # If we have reached the end of the array, add the current permutation to the result
            if start == len(nums):
                perms.append(
                    nums.copy()
                )  # Make a copy to avoid modifying the original list
                return

            # Iterate through the elements from 'start' to the end of the array
            for i in range(start, len(nums)):
                nums[start], nums[i] = (
                    nums[i],
                    nums[start],
                )  # Swap elements to create permutations
                get_permutation(
                    start + 1
                )  # Recursively generate permutations for the next index
                nums[start], nums[i] = (
                    nums[i],
                    nums[start],
                )  # Backtrack by swapping elements back

        # Start generating permutations from the beginning of the array
        get_permutation(0)
        return perms
