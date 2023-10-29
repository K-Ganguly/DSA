# LeetCode Link: https://leetcode.com/problems/permutation-in-string/
class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        # Initialize arrays to keep track of character frequencies for lowercase English letters.
        chars_freq_1 = [0] * 26  # For characters in s1
        chars_freq_2 = [0] * 26  # For characters in the sliding window of s2

        # Count the frequencies of characters in s1 and update chars_freq_1.
        for ch in s1:
            chars_freq_1[ord(ch) - ord("a")] += 1

        # Initialize pointers for the sliding window in s2.
        left = 0
        right = 0

        # Iterate through s2 with a sliding window approach.
        while right < len(s2):
            ch = s2[right]

            # Update the character frequency array for s2 with the character at the right end of the window.
            chars_freq_2[ord(ch) - ord("a")] += 1

            # Check if the window size matches the size of s1.
            if (right - left + 1) == len(s1):
                # If the character frequencies in the window match those in s1, it's a permutation.
                if chars_freq_1 == chars_freq_2:
                    return True

                # Move the left end of the window and update the character frequency array accordingly.
                ch2 = s2[left]
                chars_freq_2[ord(ch2) - ord("a")] -= 1
                left += 1

            # Move the right end of the window to expand the sliding window.
            right += 1

        # Check one final time after iterating through the entire string s2.
        if chars_freq_1 == chars_freq_2:
            return True
        else:
            return False
