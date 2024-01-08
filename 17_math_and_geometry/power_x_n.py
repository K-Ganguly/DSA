# LeetCode Link: https://leetcode.com/problems/powx-n/
class Solution:
    def myPow(self, x: float, n: int) -> float:
        # Define a helper function to calculate the power using recursive binary exponentiation
        def power(x, n):
            # Base case: if the base (x) is 0, the result is 0
            if x == 0:
                return 0
            # Base case: any non-zero number raised to the power of 0 is 1
            if n == 0:
                return 1

            # Recursive case: divide the problem into smaller subproblems
            res = power(x, n // 2)

            # Combine the results of subproblems to calculate the final result
            res = res * res

            # Adjust the result based on whether n is even or odd
            return x * res if n % 2 else res

        # Call the helper function with the absolute value of n
        res = power(x, abs(n))

        # Adjust the final result based on the sign of n
        return res if n >= 0 else 1 / res
