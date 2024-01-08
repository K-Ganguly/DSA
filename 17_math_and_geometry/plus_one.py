# LeetCode Link: https://leetcode.com/problems/plus-one/
from collections import deque


class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        # Get the length of the input digits
        L = len(digits)

        # Initialize a deque to represent the incremented number with zeros
        incremented_num = deque([0] * L)

        # Initialize the carry to 1 for the initial addition
        carry = 1

        # Iterate through the input digits from right to left
        for i in range(L - 1, -1, -1):
            # Add the current digit and the carry
            incremented_num[i] = digits[i] + carry

            # Check if there is a carry after the addition
            if incremented_num[i] > 9:
                # Update the carry and keep only the remainder
                carry = incremented_num[i] // 10
                incremented_num[i] = incremented_num[i] % 10
                print(carry)
            else:
                # Reset the carry if there is no overflow
                carry = 0

        # If there is still a carry after the iteration, add it to the leftmost side
        if carry > 0:
            incremented_num.appendleft(carry)

        # Return the final incremented number as a list
        return list(incremented_num)
