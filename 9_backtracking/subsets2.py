# LeetCode Link: https://leetcode.com/problems/subsets-ii/
class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        # Sort the input array to handle duplicates efficiently
        nums.sort()

        # Initialize an empty list to store all subsets
        subsets = list()

        # Initialize an empty list to represent the current subset being constructed
        subset = list()

        # Helper function to generate subsets starting from a specific index in the array
        def getSubset(i):
            # Base case: when the subset is complete (reached the end of the array)
            if i == len(nums):
                # Add the current subset to the list of subsets
                subsets.append(subset.copy())
                return

            # Include the current element in the subset and move to the next index
            subset.append(nums[i])
            getSubset(i + 1)

            # Exclude the current element and continue with the next index
            subset.pop()

            # Skip duplicates to avoid duplicate subsets
            while i < len(nums) - 1 and nums[i] == nums[i + 1]:
                i += 1

            # Continue generating subsets with the next unique element
            getSubset(i + 1)

        # Start generating subsets from the beginning of the array
        getSubset(0)

        # Return the final list of subsets
        return subsets
