# LeetCode Link: https://leetcode.com/problems/longest-substring-without-repeating-characters/
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # Initialize a dictionary to store the most recent index where each character was seen.
        chars_index = dict()
        # Initialize variables to keep track of the maximum length of a substring and the left pointer.
        max_len_substr = 0
        left = 0

        # Iterate through the string using a right pointer.
        for right in range(len(s)):
            # Check if the current character is already in the dictionary (i.e., it has been seen before)
            # and if its index is greater than or equal to the current left pointer.
            if s[right] in chars_index and chars_index[s[right]] >= left:
                # If yes, update the left pointer to the index after the last occurrence of the current character.
                left = chars_index[s[right]] + 1
            # Update the index of the current character in the dictionary.
            chars_index[s[right]] = right
            # Calculate the current length of the substring and update the maximum length if it's longer.
            max_len_substr = max(max_len_substr, (right - left + 1))

        # Return the maximum length of a substring without repeating characters.
        return max_len_substr
