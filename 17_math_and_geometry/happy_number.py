# LeetCode Link: https://leetcode.com/problems/happy-number/
class Solution:
    def isHappy(self, n: int) -> bool:
        # Define a helper function to calculate the sum of squares of digits
        def sum_of_squares(n):
            sum_sq = 0
            # Extract each digit and add its square to the sum
            while n > 0:
                digit = n % 10
                n = n // 10
                sum_sq += digit**2
            return sum_sq

        # Use a set to keep track of visited numbers and detect cycles
        visited = set()

        # Continue the process until the number becomes 1 (happy) or a cycle is detected (not happy)
        while n not in visited:
            # Add the current number to the set of visited numbers
            visited.add(n)

            # Calculate the sum of squares of digits for the current number
            n = sum_of_squares(n)

            # If the sum becomes 1, the number is happy, and the loop can be terminated
            if n == 1:
                return True

        # If the loop completes without finding 1, the number is not happy
        return False
