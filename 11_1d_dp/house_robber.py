# LeetCode Link: https://leetcode.com/problems/house-robber/
# Approach 1: Recursion with Memoization
class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)
        money_collected = [None] * (n + 1)

        def findMoney(i):
            # Base case: If the index is beyond the array, return 0
            if i >= n:
                return 0
            # If the money collected at this index is not calculated yet, calculate it
            if money_collected[i] == None:
                # Calculate the money collected considering robbing the current house or skipping it
                money_1 = nums[i] + findMoney(i + 2)
                money_2 = findMoney(i + 1)
                # Update the money collected at the current index
                money_collected[i] = max(money_1, money_2)
            # Return the money collected at the current index
            return money_collected[i]

        # Start the recursion from the first house
        findMoney(0)
        # Return the maximum money collected
        return money_collected[0]


# Approach 2: DP
class Solution:
    def rob(self, nums: List[int]) -> int:
        money_1 = 0
        money_2 = 0
        n = len(nums)
        for num in nums:
            # Calculate the maximum money collected at the current house considering robbing or skipping
            temp = max(money_1 + num, money_2)
            # Update the money collected for the next iteration
            money_1 = money_2
            money_2 = temp
        # Return the maximum money collected
        return money_2
