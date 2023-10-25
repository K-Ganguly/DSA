# LeetCode Link: https://leetcode.com/problems/generate-parentheses/
class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        # Initialize an empty list to store valid combinations.
        parens_list = list()
        # Initialize an empty string to build the combinations.
        s = ""

        def generate(open, close, s, parens_list):
            # If we can still open a parenthesis, add an opening parenthesis '('.
            if open > 0:
                generate(open - 1, close, s + "(", parens_list)
            # If there are unmatched opening parentheses, add a closing parenthesis ')'.
            if open < close:
                generate(open, close - 1, s + ")", parens_list)
            # When there are no remaining open and close parentheses, we have a valid combination.
            if open == 0 and close == 0:
                parens_list.append(s)

        # Start the recursive generation with n open and n close parentheses.
        generate(n, n, s, parens_list)
        # Return the list of valid combinations.
        return parens_list
