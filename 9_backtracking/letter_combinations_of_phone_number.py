# LeetCode Link: https://leetcode.com/problems/letter-combinations-of-a-phone-number/
class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        # Dictionary mapping each digit to its corresponding characters
        digits_to_char = {
            "2": "abc",
            "3": "def",
            "4": "ghi",
            "5": "jkl",
            "6": "mno",
            "7": "pqrs",
            "8": "tuv",
            "9": "wxyz",
        }

        # Initialize a list to store all possible letter combinations
        letter_combs = list()

        # Helper function for depth-first search to generate combinations
        def dfs(i, combination):
            # If the current index exceeds the length of the digits,
            # the current combination is valid, so add it to the result list
            if i >= len(digits):
                letter_combs.append(combination)
                return

            # Get the characters corresponding to the current digit
            chars = digits_to_char[digits[i]]

            # Iterate through the characters and recursively call the dfs function
            for ch in chars:
                dfs(i + 1, combination + ch)

        # Check if the input digits are not empty
        if digits:
            # Start the depth-first search from the first digit with an empty initial combination
            dfs(0, "")

        # Return the list of all valid letter combinations
        return letter_combs
