# LeetCode Link: https://leetcode.com/problems/minimum-interval-to-include-each-query/
import heapq


class Solution:
    def minInterval(self, intervals: List[List[int]], queries: List[int]) -> List[int]:
        # Sort intervals based on their start times
        intervals.sort()

        # Dictionary to store the result for each query
        res = {}

        # Min heap to keep track of intervals with minimum lengths
        min_heap = list()

        # Initialize index for traversing intervals
        i = 0

        # Iterate through sorted queries
        for q in sorted(queries):
            # Process intervals whose start time is less than or equal to the current query
            while i < len(intervals) and intervals[i][0] <= q:
                lb, ub = intervals[i]
                # Add interval length and end time to the min heap
                heapq.heappush(min_heap, ((ub - lb + 1), ub))
                i += 1

            # Remove intervals from the heap whose end time is less than the current query
            while min_heap and min_heap[0][1] < q:
                heapq.heappop(min_heap)

            # Store the result for the current query: minimum interval length in the heap
            # If the heap is empty, set the result to -1
            res[q] = min_heap[0][0] if min_heap else -1

        # Return a list of results for each query
        return [res[q] for q in queries]
