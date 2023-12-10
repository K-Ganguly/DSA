# LeetCode Link: https://leetcode.com/problems/house-robber-ii/
class Solution:
    def rob(self, nums: List[int]) -> int:
        def findMoney(start, end):
            # Initialize variables to track money collected at two consecutive houses
            money1, money2 = 0, 0
            # Iterate through the specified range of houses
            for i in range(start, (end + 1)):
                # Calculate the maximum money collected at the current house considering robbing or skipping
                temp = max(money1 + nums[i], money2)
                # Update the money collected for the next iteration
                money1 = money2
                money2 = temp
            # Return the maximum money collected in the specified range
            return money2

        # Calculate the maximum money collected for the first set of houses (excluding the last house)
        first_house = findMoney(0, len(nums) - 2)
        # Calculate the maximum money collected for the second set of houses (excluding the first house)
        last_house = findMoney(1, len(nums) - 1)
        # Return the maximum money collected considering robbing either the first house, last house, or both
        return max(nums[0], first_house, last_house)
