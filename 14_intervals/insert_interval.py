# LeetCode Link: https://leetcode.com/problems/insert-interval/
class Solution:
    def insert(
        self, intervals: List[List[int]], newInterval: List[int]
    ) -> List[List[int]]:
        # Initialize a list to store the merged intervals
        new_intervals = list()

        # Iterate through existing intervals
        for i, interval in enumerate(intervals):
            lb = interval[0]  # Lower bound of the current interval
            ub = interval[1]  # Upper bound of the current interval
            new_lb = newInterval[0]  # Lower bound of the new interval to be inserted
            new_ub = newInterval[1]  # Upper bound of the new interval to be inserted

            # If the upper bound of the new interval is less than the lower bound of the current interval,
            # insert the new interval and all remaining intervals, then return the result
            if new_ub < lb:
                new_intervals.append(newInterval)
                new_intervals += intervals[i:]
                return new_intervals

            # If the lower bound of the new interval is greater than the upper bound of the current interval,
            # simply add the current interval to the result
            elif new_lb > ub:
                new_intervals.append(interval)

            # If there is an overlap between the current interval and the new interval,
            # merge them by updating the new interval's bounds
            else:
                newInterval = [min(lb, new_lb), max(ub, new_ub)]

        # Add the merged or non-overlapping new interval to the result
        new_intervals.append(newInterval)

        # Return the final list of merged intervals
        return new_intervals
