# LeetCode Link: https://leetcode.com/problems/coin-change/
# Approach 1: Recursion with Memoization
class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        num_coins = [float("inf")] * (amount + 1)

        def find_num_coins(remaining_amt):
            if remaining_amt == 0:
                return 0
            if remaining_amt < 0:
                return -1
            if num_coins[remaining_amt] != float("inf"):
                return num_coins[remaining_amt]
            min_coins = float("inf")
            for coin in coins:
                next_amt = remaining_amt - coin
                num_coins_for_amt = find_num_coins(next_amt)
                if num_coins_for_amt != -1:
                    min_coins = min(min_coins, 1 + num_coins_for_amt)

            num_coins[remaining_amt] = -1 if min_coins == float("inf") else min_coins
            return num_coins[remaining_amt]

        min_num_coins = find_num_coins(amount)
        return min_num_coins


# Approach 2: DP-Basic
class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        num_coins = [float("inf")] * (amount + 1)
        num_coins[0] = 0
        for amt in range(1, amount + 1):
            min_coins = float("inf")
            for coin in coins:
                next_amt = amt - coin
                num_coins_for_amt = (1 + num_coins[next_amt]) if next_amt >= 0 else -1
                if num_coins_for_amt != -1:
                    min_coins = min(min_coins, num_coins_for_amt)
            num_coins[amt] = min_coins
        return num_coins[amount] if num_coins[amount] != float("inf") else -1
