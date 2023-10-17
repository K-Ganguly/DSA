# LeetCode Link: https://leetcode.com/problems/valid-parentheses/
class Solution:
    def isValid(self, s: str) -> bool:
        brackets = list()  # Initialize a list to keep track of opening brackets.
        matching_parentheses = {
            ")": "(",
            "}": "{",
            "]": "[",
        }  # Create a mapping of closing to opening brackets.
        opening_brackets = set(
            matching_parentheses.values()
        )  # Create a set of opening brackets for quick lookup.

        for ch in s:
            if ch in opening_brackets:
                brackets.append(
                    ch
                )  # If the character is an opening bracket, add it to the stack.
            else:
                # If the character is a closing bracket, check if it matches the top of the stack.
                if (len(brackets) == 0) or (brackets[-1] != matching_parentheses[ch]):
                    return False  # If not, it's an invalid expression.
                brackets.pop()  # Remove the matching opening bracket from the stack.

        if len(brackets) > 0:
            return False  # If there are remaining opening brackets, it's an invalid expression.
        return True  # If all brackets are correctly matched and balanced, it's a valid expression.
