# LeetCode Link: https://leetcode.com/problems/palindromic-substrings/description/
class Solution:
    def countSubstrings(self, s: str) -> int:
        # Helper function to count palindromic substrings expanding from the center
        def get_num_palindromes(left, right):
            num_palins = 0
            # Expand the palindrome substring while characters match
            while left > -1 and right < len(s) and s[left] == s[right]:
                num_palins += 1
                left -= 1
                right += 1
            return num_palins

        num_palins = 0

        # Iterate through each character in the string as a potential center of palindrome
        for i in range(len(s)):
            # Check for odd-length and even-length palindromes
            for l, r in ((i, i), (i, i + 1)):
                num_palins += get_num_palindromes(l, r)

        return num_palins
