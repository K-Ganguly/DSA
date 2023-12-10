# LeetCode Link: https://leetcode.com/problems/climbing-stairs/
# Approach 1: Recursion with Memoization
class Solution:
    def climbStairs(self, n: int) -> int:
        numWays = [0] * (n + 1)

        def findWays(i):
            nonlocal numWays
            # If already computed, return the result
            if numWays[i] > 0:
                return numWays[i]
            # Base case: If reached the top, there is 1 way
            if i == n:
                numWays[i] = 1
                return numWays[i]
            # If exceeded the top, there are 0 ways
            if i > n:
                return 0
            # Recursively calculate ways for the current step and store the result
            numWays[i] = findWays(i + 1) + findWays(i + 2)
            return numWays[i]

        # Start recursion from the bottom (step 0)
        findWays(0)
        return numWays[0]


# Approach 2: DP-Tabulation-Basic
class Solution:
    def climbStairs(self, n: int) -> int:
        # Initialize an array to store ways for each step
        dp = [0] * (n + 1)
        # Base cases: there is 1 way to reach the top from the top and the step below
        dp[n] = 1
        dp[n - 1] = 1
        # Iterate from the second-to-last step to the bottom, filling the array
        for i in range((n - 2), -1, -1):
            dp[i] = dp[i + 1] + dp[i + 2]
        # Return the result for the bottom step
        return dp[0]


# Approach 3: DP-Tabulation-Space Optimization
class Solution:
    def climbStairs(self, n: int) -> int:
        # Initialize variables to store ways for the last two steps
        left = 1
        right = 1
        # Iterate from the second-to-last step to the bottom, updating variables
        for i in range((n - 2), -1, -1):
            temp = left
            left = left + right
            right = temp
        # Return the result for the bottom step
        return left
