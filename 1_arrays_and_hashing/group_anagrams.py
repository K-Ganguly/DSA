# Leetcode Link: https://leetcode.com/problems/group-anagrams/
from collections import defaultdict


class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagram_groups = defaultdict(list)
        for word in strs:
            char_freq = [0] * 26
            for ch in word:
                char_index = ord(ch) - ord("a")
                char_freq[char_index] += 1
            anagram_groups[tuple(char_freq)].append(word)
        return list(anagram_groups.values())
