# LeetCode Link: https://leetcode.com/problems/sum-of-two-integers/
class Solution:
    def getSum(self, a: int, b: int) -> int:
        # Set a mask to limit the result to 32 bits
        mask = 0xFFFFFFFF

        # Continue the addition until there is no carry left
        while (mask & b) > 0:
            # XOR adds bits without considering carry, and the AND with left shift calculates the carry
            a, b = a ^ b, (a & b) << 1

        # If there is still a carry, take the 32-bit result using the mask, otherwise return the result
        return (mask & a) if b > 0 else a
