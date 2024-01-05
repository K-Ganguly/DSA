# https://leetcode.com/problems/reverse-integer/
import math


class Solution:
    def reverse(self, x: int) -> int:
        # Integer.MAX_VALUE = 2147483647 (ends with 7)
        # Integer.MIN_VALUE = -2147483648 (ends with -8)

        MIN = -2147483648  # -2^31,
        MAX = 2147483647  #  2^31 - 1

        res = 0  # Initialize the reversed number

        # Continue the loop until x becomes 0
        while x:
            digit = int(math.fmod(x, 10))  # Extract the last digit of x
            x = int(x / 10)  # Update x by removing the last digit

            # Check for integer overflow for positive numbers
            if res > MAX // 10 or (res == MAX // 10 and digit > MAX % 10):
                return 0

            # Check for integer overflow for negative numbers
            if res < MIN // 10 or (res == MIN // 10 and digit < MIN % 10):
                return 0

            # Update the reversed number by adding the last digit
            res = (res * 10) + digit

        return res  # Return the reversed number
