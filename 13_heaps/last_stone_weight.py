# LeetCode Link: https://leetcode.com/problems/last-stone-weight/
import heapq


class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        # Convert the stones to their negative values and heapify the list
        stones = [-s for s in stones]
        heapq.heapify(stones)

        # Continue until there is only one stone left (or none)
        while len(stones) > 1:
            # Remove the two heaviest stones
            stone1 = heapq.heappop(stones)
            stone2 = heapq.heappop(stones)

            # Calculate the result of the collision (crash)
            crash = -1 * abs(stone1 - stone2)

            # If the crash result is not zero, add it back to the heap
            if crash != 0:
                heapq.heappush(stones, crash)

        # If there are no stones left, the result is zero; otherwise, return the last remaining stone's weight
        if len(stones) == 0:
            return 0
        else:
            return -stones[0]
