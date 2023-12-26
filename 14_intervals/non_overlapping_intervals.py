# LeetCode Link: https://leetcode.com/problems/non-overlapping-intervals/
class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        # Sort intervals based on the start time
        intervals.sort()

        # Initialize variables to keep track of the previous end time,
        # the length of intervals, and the number of intervals to be removed
        prev_end = intervals[0][1]
        L = len(intervals)
        num_removals = 0

        # Iterate through the sorted intervals starting from the second interval
        for i in range(1, L):
            start, end = intervals[i]

            # If the previous interval's end time is less than or equal to
            # the current interval's start time, they don't overlap, and we update prev_end
            if prev_end <= start:
                prev_end = end
            else:
                # If they overlap, we need to remove one interval, so increment the removal count
                num_removals += 1
                # Update prev_end to the minimum of the current interval's end time
                # and the previous interval's end time to ensure we remove the one with
                # the larger end time
                prev_end = min(prev_end, end)

        # Return the total number of intervals to be removed
        return num_removals
