# LeetCode Link: https://leetcode.com/problems/min-cost-climbing-stairs/
# Approach 1: Recursion with Memoization
class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        n = len(cost)
        min_cost = [0] * (n + 1)

        def findCost(i):
            # Base case: If the index is beyond the array, return 0
            if i >= n:
                return 0
            # If the minimum cost at this index is not calculated yet, calculate it
            if min_cost[i] == 0:
                # Calculate the cost of advancing one step and two steps
                cost_1 = findCost(i + 1)
                cost_2 = findCost(i + 2)
                # Update the minimum cost at the current index
                min_cost[i] = cost[i] + min(cost_1, cost_2)
            # Return the minimum cost at the current index
            return min_cost[i]

        # Start the recursion from the first step
        findCost(0)
        # Return the minimum cost of starting from the first or second step
        return min(min_cost[0], min_cost[1])


# Approach 2: DP
class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        n = len(cost)
        # Add a zero at the end to handle the case when reaching the top from the last step
        cost.append(0)
        # Start the iteration from the second-to-last step
        start = n - 2
        for i in range(start, -1, -1):
            # Update the cost at each step by adding the minimum cost of advancing one step or two steps
            cost[i] += min(cost[i + 1], cost[i + 2])
        # Return the minimum cost of starting from the first or second step
        return min(cost[0], cost[1])
