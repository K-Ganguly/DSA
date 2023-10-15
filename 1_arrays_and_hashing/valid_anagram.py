# Leetcode Link: https://leetcode.com/problems/valid-anagram/
from collections import defaultdict


class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        num_chars = defaultdict(int)
        for char in s:
            num_chars[char] += 1
        for char in t:
            num_chars[char] -= 1
            if num_chars[char] == 0:
                num_chars.pop(char)
        if len(num_chars) == 0:
            return True
        else:
            return False
