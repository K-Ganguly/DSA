# LeetCode Link: https://leetcode.com/problems/search-in-rotated-sorted-array/
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        low = 0
        high = len(nums) - 1

        # Calculate the middle index of the current search range.
        while low <= high:
            mid = low + (high - low) // 2

            # Check if the middle element is equal to the target.
            if nums[mid] == target:
                return mid

            if nums[low] <= nums[mid]:
                # If the left half of the array is sorted or has no rotation:
                if nums[low] <= target < nums[mid]:
                    # If the target is in the left half, update the high bound.
                    high = mid - 1
                else:
                    # Otherwise, update the low bound to search the right half.
                    low = mid + 1
            else:
                # If the right half of the array is sorted or has no rotation:
                if nums[mid] < target <= nums[high]:
                    # If the target is in the right half, update the low bound.
                    low = mid + 1
                else:
                    # Otherwise, update the high bound to search the left half.
                    high = mid - 1

        # If the target is not found in the array, return -1.
        return -1
