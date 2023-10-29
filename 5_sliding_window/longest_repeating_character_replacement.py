# LeetCode Link: https://leetcode.com/problems/longest-repeating-character-replacement/description/
class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        chars_freq = [0] * 26
        left = 0
        right = 0
        max_freq = 0
        max_len = 0

        while right < len(s):
            # Calculate the character frequency and update the maximum character frequency.
            ch1 = s[right]
            ch1_idx = ord(ch1) - ord("A")
            chars_freq[ch1_idx] += 1
            max_freq = max(max_freq, chars_freq[ch1_idx])

            # Calculate the number of replacements needed to make the window valid.
            replacements = (right - left + 1) - max_freq

            if replacements > k:
                # If replacements exceed the given limit (k), move the left pointer to shrink the window.
                ch2 = s[left]
                chars_freq[ord(ch2) - ord("A")] -= 1
                left += 1

            # Update maximum length of the valid substring.
            max_len = max(max_len, (right - left + 1))

            right += 1  # Move the right pointer to expand the window.

        return max_len
