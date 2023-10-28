# LeetCode Link: https://leetcode.com/problems/find-minimum-in-rotated-sorted-array/
class Solution:
    def findMin(self, nums: List[int]) -> int:
        low = 0
        high = len(nums) - 1

        # Check if the array is not rotated; if not, the minimum is at index 'low.'
        if nums[low] <= nums[high]:
            return nums[low]

        # Start binary search when the array is rotated.
        while low < high:
            mid = low + (high - low) // 2

            # If the middle element is greater than the element at 'high',
            # it means the pivot point (rotation point) is on the right side of 'mid.'
            # We update 'low' to 'mid + 1' to search in the right subarray.
            if nums[mid] > nums[high]:
                low = mid + 1
            else:
                # If the middle element is less than or equal to the element at 'high',
                # it means the pivot point is on the left side of 'mid.'
                # We update 'high' to 'mid' to search in the left subarray.
                high = mid

        # When the loop exits, 'low' will be pointing to the minimum element.
        return nums[low]
