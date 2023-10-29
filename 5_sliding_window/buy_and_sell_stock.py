# LeetCode Link: https://leetcode.com/problems/best-time-to-buy-and-sell-stock/
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # Initialize the maximum profit to 0 and the initial buying price to the first day's price.
        max_profit = 0
        boughtAt = prices[0]

        # Iterate through the prices on each day.
        for price in prices:
            # If the current day's price is greater than or equal to the buying price:
            if price >= boughtAt:
                # Calculate the current profit by selling at the current price.
                curr_profit = price - boughtAt
                # Update the maximum profit if the current profit is higher.
                max_profit = max(max_profit, curr_profit)
            else:
                # If the current day's price is lower than the buying price, update the buying price.
                boughtAt = price
        # Return the maximum profit obtained from the entire sequence of prices.
        return max_profit
