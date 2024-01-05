# LeetCode Link: https://leetcode.com/problems/number-of-1-bits/
# Approach 1:
class Solution:
    def hammingWeight(self, n: int) -> int:
        # Initialize the result variable to 0
        res = 0

        # Iterate until 'n' becomes 0
        while n:
            # Add the last bit of 'n' to the result
            res += n % 2

            # Right shift 'n' by 1 to discard the last bit
            n = n >> 1

        # Return the count of set bits (number of '1's) in the binary representation of the original 'n'
        return res


# Approach 2:
class Solution:
    def hammingWeight(self, n: int) -> int:
        # Initialize the result variable to 0
        res = 0

        # Iterate until 'n' becomes 0
        while n:
            # Increment the result since the rightmost set bit is found
            res += 1

            # Turn off the rightmost set bit by performing n & (n-1)
            # This operation flips the rightmost '1' bit to '0'
            n = n & (n - 1)

        # Return the count of set bits (number of '1's) in the binary representation of the original 'n'
        return res
