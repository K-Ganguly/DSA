# LeetCode Link: https://leetcode.com/problems/valid-anagram/
from collections import defaultdict


class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        num_chars = defaultdict(int)

        # Count the characters in the first string.
        for char in s:
            num_chars[char] += 1

        # Compare and decrement characters in the second string.
        for char in t:
            num_chars[char] -= 1
            if num_chars[char] == 0:
                num_chars.pop(char)

        # If there are no remaining characters in the dictionary, they are anagrams.
        if len(num_chars) == 0:
            return True
        else:
            return False
