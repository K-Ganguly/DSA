# LeetCode Link: https://leetcode.com/problems/valid-parenthesis-string/
class Solution:
    def checkValidString(self, s: str) -> bool:
        # Initialize counts for open and close parentheses
        open_count, close_count = 0, 0

        # Iterate through each character in the string
        for char in s:
            # Update counts based on the type of character encountered
            if char == "(":
                # Treat '(' as both open and close, increment both counts
                open_count, close_count = open_count + 1, close_count + 1
            elif char == ")":
                # Decrement both counts for a closing parenthesis
                open_count, close_count = open_count - 1, close_count - 1
            else:
                # Treat '*' as both open and close, decrement open count, increment close count
                open_count, close_count = open_count - 1, close_count + 1

            # Check if the close count becomes negative; if yes, the string is invalid
            if close_count < 0:
                return False

            # If open count becomes negative, reset it to 0 as '*' can be considered empty
            if open_count < 0:
                open_count = 0

        # After processing the entire string, check if open count is 0, indicating a valid string
        return open_count == 0
