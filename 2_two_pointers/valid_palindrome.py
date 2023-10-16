# LeetCode Link: https://leetcode.com/problems/valid-palindrome/
class Solution:
    def isPalindrome(self, s: str) -> bool:
        i = 0  # Initialize a pointer for the start of the string.
        j = len(s) - 1  # Initialize a pointer for the end of the string.

        while i < j:
            # Move the left pointer to the right until it points to an alphanumeric character.
            while i < j and not s[i].isalnum():
                i += 1

            # Move the right pointer to the left until it points to an alphanumeric character.
            while i < j and not s[j].isalnum():
                j -= 1

            # Check if the characters at the pointers (case-insensitive) are not equal.
            if s[i].lower() != s[j].lower():
                return False  # If they are not equal, it's not a palindrome.

            i += 1  # Move the left pointer to the right.
            j -= 1  # Move the right pointer to the left.

        return True  # If all characters were equal (ignoring non-alphanumeric), it's a valid palindrome.


# The code above efficiently checks whether a given string is a valid palindrome.
# It uses two pointers (i and j) that move towards each other while ignoring non-alphanumeric characters
# and comparing characters case-insensitively. If all characters match, it's considered a valid palindrome.
