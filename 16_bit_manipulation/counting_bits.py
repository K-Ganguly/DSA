# LeetCode Link: https://leetcode.com/problems/counting-bits/
class Solution:
    def countBits(self, n: int) -> List[int]:
        # Create a list to store the count of set bits for each number from 0 to n
        dp = [0] * (n + 1)

        # Initialize an offset to track powers of 2
        offset = 1

        # Iterate through the numbers from 1 to n
        for i in range(1, n + 1):
            # If the current number is a power of 2, update the offset
            if offset * 2 == i:
                offset = i

            # The count of set bits for the current number is 1 plus the count of set bits for the corresponding offset
            dp[i] = 1 + dp[i - offset]

        # Return the list containing the count of set bits for each number from 0 to n
        return dp
