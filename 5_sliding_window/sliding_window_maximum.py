# LeetCode Link: https://leetcode.com/problems/sliding-window-maximum/
from collections import deque


class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        left = 0
        right = 0
        L = len(nums)
        max_window = []
        max_queue = deque()

        while right < L:
            while max_queue and max_queue[-1] < nums[right]:
                max_queue.pop()  # Remove smaller elements from the deque.

            max_queue.append(nums[right])  # Add the current element to the deque.

            if (right - left + 1) == k:
                max_window.append(
                    max_queue[0]
                )  # Append the maximum of the current window.

                if nums[left] == max_queue[0]:
                    max_queue.popleft()  # If the leftmost element is the maximum, remove it.

                left += 1  # Slide the window by moving the left pointer.

            right += 1  # Expand the sliding window to the right.

        return max_window  # Return the list of maximum values for each sliding window.
