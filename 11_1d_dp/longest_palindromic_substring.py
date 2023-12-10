# LeetCode Link: https://leetcode.com/problems/longest-palindromic-substring/
class Solution:
    def longestPalindrome(self, s: str) -> str:
        # Initialize variables to keep track of the longest palindrome substring
        palindrome_str = ""
        palindrome_str_len = 0
        max_left = 0
        max_right = 0

        # Helper function to check if a palindrome exists expanding from the center
        def check_palindrome(left, right):
            nonlocal palindrome_str
            nonlocal palindrome_str_len
            nonlocal max_left
            nonlocal max_right

            # Expand the palindrome substring while characters match
            while left > -1 and right < len(s) and s[left] == s[right]:
                # Update if a longer palindrome is found
                if (right - left + 1) > palindrome_str_len:
                    palindrome_str_len = right - left + 1
                    max_left = left
                    max_right = right
                left -= 1
                right += 1

        # Iterate through each character in the string as a potential center of palindrome
        for i in range(0, len(s)):
            check_palindrome(i, i)  # Check for odd-length palindrome
            check_palindrome(i, i + 1)  # Check for even-length palindrome

        # Extract the longest palindrome substring from the original string
        palindrome_str = s[max_left : (max_right + 1)]

        return palindrome_str
