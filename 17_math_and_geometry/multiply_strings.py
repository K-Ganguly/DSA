# LeetCode Link: https://leetcode.com/problems/multiply-strings/
class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        # Check if either of the numbers is zero, in which case the result is zero
        if "0" in [num1, num2]:
            return "0"

        # Reverse the input numbers for easier iteration from right to left
        num1 = num1[::-1]
        num2 = num2[::-1]

        # Get the lengths of the reversed numbers
        M = len(num1)
        N = len(num2)

        # Initialize an array to store the result, with enough space for the product
        num = [0] * (M + N)

        # Iterate through each digit of both numbers and calculate the product
        for i in range(M):
            for j in range(N):
                product = int(num1[i]) * int(num2[j])

                # Add the current product to the corresponding position in the result array
                num[i + j] += product

                # Extract the digit and carry from the sum
                digit = num[i + j] % 10
                carry = num[i + j] // 10

                # Update the current position to store only the remainder after carry
                num[i + j] = digit

                # Add the carry to the next position
                num[i + j + 1] += carry

        # Reverse the result array and find the position where non-zero digits start
        num = num[::-1]
        start = 0
        while start < (M + N) and num[start] == 0:
            start += 1

        # Convert the result array to a string and return the product
        num = list(map(str, num[start:]))
        product = "".join(num)
        return product
