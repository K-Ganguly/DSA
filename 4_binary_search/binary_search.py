# LeetCode Link: https://leetcode.com/problems/binary-search/
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        # Initialize left and right pointers to the beginning and end of the array.
        left = 0
        right = len(nums) - 1

        # Perform binary search while the left pointer is less than or equal to the right pointer.
        while left <= right:
            # Calculate the middle index.
            mid = left + (right - left) // 2

            # Check if the middle element is equal to the target.
            if nums[mid] == target:
                return mid
            # If the middle element is less than the target, update the left pointer to search the right half.
            if nums[mid] < target:
                left = mid + 1
            # If the middle element is greater than the target, update the right pointer to search the left half.
            elif nums[mid] > target:
                right = mid - 1

        # If the target is not found in the array, return -1.
        return -1
