# LeetCode Link: https://leetcode.com/problems/merge-intervals/
class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        # Sort the intervals based on their start values
        intervals.sort()

        # Initialize a list to store the merged intervals, starting with the first interval
        merged_intervals = [intervals[0]]

        # Iterate through the sorted intervals
        for interval in intervals:
            lb, ub = interval  # Lower and upper bounds of the current interval
            last_ub = merged_intervals[-1][1]  # Upper bound of the last merged interval

            # If there is an overlap between the current interval and the last merged interval,
            # update the upper bound of the last merged interval to include the current interval
            if lb <= last_ub:
                merged_intervals[-1][1] = max(last_ub, ub)
            else:
                # If there is no overlap, add the current interval to the list of merged intervals
                merged_intervals.append(interval)

        # Return the final list of merged intervals
        return merged_intervals
