# https://leetcode.com/problems/reverse-bits/
class Solution:
    def reverseBits(self, n: int) -> int:
        # Initialize a variable to store the reversed number
        reversed_num = 0

        # Iterate through each bit position (32 bits in total for a 32-bit integer)
        for i in range(32):
            # Extract the rightmost bit of the original number using bitwise AND with 1
            nth_bit = n & 1

            # Right shift the original number by 1 to move to the next bit
            n >>= 1

            # Update the reversed number by setting the current bit position to nth_bit
            # The new bit is placed at the position determined by (31 - i), effectively reversing the bit order
            reversed_num |= nth_bit << (31 - i)

        # Return the final reversed number
        return reversed_num
