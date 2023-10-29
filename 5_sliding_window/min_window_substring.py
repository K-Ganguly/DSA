# LeetCode Link: https://leetcode.com/problems/minimum-window-substring/description/
from collections import defaultdict


class Solution:
    def minWindow(self, s: str, t: str) -> str:
        # Initialize a dictionary to store character frequencies of the target string 't'.
        char_freq = defaultdict(int)
        window = ""  # Initialize the resulting window.
        min_window_len = float(
            "inf"
        )  # Initialize the minimum window length as infinity.

        # Count the character frequencies in the target string 't'.
        for ch in t:
            char_freq[ch] += 1

        window_start = 0
        left = 0
        right = 0
        num_chars = len(char_freq)

        while right < len(s):
            ch = s[right]
            if ch in char_freq:
                char_freq[ch] -= 1
                if char_freq[ch] == 0:
                    num_chars -= 1

            # When all required characters are found in the current window:
            while num_chars == 0:
                # Check if the current window is smaller than the previously smallest window.
                if (right - left + 1) < min_window_len:
                    min_window_len = right - left + 1
                    window_start = left  # Update the start of the minimum window.

                ch1 = s[left]

                if ch1 in char_freq:
                    char_freq[s[left]] += 1
                    if char_freq[s[left]] == 1:
                        num_chars += 1

                left += 1  # Move the left pointer to try to find a smaller window.

            right += 1  # Move the right pointer to expand the window.

        # Get the substring that represents the minimum window.
        window = (
            s[window_start : (window_start + min_window_len)]
            if min_window_len < float("inf")
            else ""
        )

        return window  # Return the minimum window substring that contains all characters of 't'.
