# LeetCode Link: https://leetcode.com/problems/two-sum-ii-input-array-is-sorted/
class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        i = 0  # Initialize the left pointer.
        j = len(numbers) - 1  # Initialize the right pointer.

        while i < j:
            number_sum = (
                numbers[i] + numbers[j]
            )  # Calculate the sum of the elements at pointers.

            if number_sum == target:
                # If the sum matches the target, return the indices of the two numbers.
                return [(i + 1), (j + 1)]
            elif number_sum < target:
                i += 1  # If the sum is too small, move the left pointer to consider a larger number.
            else:
                j -= 1  # If the sum is too large, move the right pointer to consider a smaller number.


# The code above efficiently uses two pointers (i and j) to find a pair of numbers in the sorted array
# that sum up to the target. The pointers move inward, reducing the search space with each iteration.
# The solution leverages the fact that the array is sorted to optimize the search.
