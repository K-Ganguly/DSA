# LeetCode Link: https://leetcode.com/problems/partition-equal-subset-sum/
# Approach 1: Recursion with Memoization
class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        num_sum = sum(nums)
        if num_sum % 2 != 0:
            return False
        target = num_sum // 2
        n = len(nums)
        # Create a 2D array for memoization
        memo = [[-1] * (target + 1) for _ in range(n)]

        def checkSum(i, target):
            if target == 0:
                return True
            if i >= n or target < 0:
                return False
            if memo[i][target] != -1:
                return memo[i][target]
            # taking nums[i]
            taking = checkSum(i + 1, target - nums[i])
            # not taking nums[i]
            not_taking = checkSum(i + 1, target)
            # Update the memo array with the result of the current subproblem
            memo[i][target] = taking or not_taking
            # Return the result of the current subproblem
            return memo[i][target]

        # Return the result of the initial subproblem
        return checkSum(0, target)


# Approach 2: DP - Basic
class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        num_sum = sum(nums)
        # If the sum is not even, partition is not possible
        if num_sum % 2 != 0:
            return False
        target = num_sum // 2
        n = len(nums)
        # Create a 2D array for dynamic programming
        dp = [[False] * (target + 1) for _ in range(n + 1)]
        # Base case: an empty subset can achieve a sum of 0
        for i in range(n + 1):
            dp[i][0] = True
        # Build the DP table bottom-up
        for i in range(1, n + 1):
            for t in range(1, target + 1):
                # If the current number can be included
                if t >= nums[i - 1]:
                    dp[i][t] = dp[i - 1][t] or dp[i - 1][t - nums[i - 1]]
                else:
                    dp[i][t] = dp[i - 1][t]
        # The final result is stored in the bottom-right cell of the DP table
        return dp[n][target]


# Approach 3: DP-Optimized
class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        # Calculate the sum of the numbers in the array
        nums_sum = sum(nums)
        # If the sum is not even, partition is not possible
        if nums_sum % 2 != 0:
            return False
        # Calculate the target sum for each partition
        target = nums_sum // 2
        # Initialize a set to store possible sums using dynamic programming
        dp = set()
        # Add the base case: an empty subset can achieve a sum of 0
        dp.add(0)
        # Iterate through each number in the array
        for num in nums:
            # Create a new set to store possible sums for the current iteration
            next_dp = set()
            # Iterate through sums stored in the current dp set
            for t in dp:
                # If the target sum is achieved, return True
                if target == t + num:
                    return True
                # Add the current number to the sums in dp
                next_dp.add(t + num)
                # Preserve the current sum in dp without using the current number
                next_dp.add(t)
            # Update dp with the set of sums for the current iteration
            dp = next_dp
        # If no subset is found to achieve the target sum, return False
        return False
