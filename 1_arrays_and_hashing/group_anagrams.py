# LeetCode Link: https://leetcode.com/problems/group-anagrams/
from collections import defaultdict


class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # Create a dictionary to group anagrams by their character frequency patterns.
        anagram_groups = defaultdict(list)

        # Iterate through each word in the input list.
        for word in strs:
            # Create a list to count the occurrence of each character in the word.
            char_freq = [0] * 26

            # Calculate the character frequency of each character in the word.
            for ch in word:
                # Determine the index of the character in the character frequency list.
                char_index = ord(ch) - ord("a")
                # Increment the count of that character in the frequency list.
                char_freq[char_index] += 1

            # Use the character frequency pattern (as a tuple) as a key in the dictionary to group anagrams.
            anagram_groups[tuple(char_freq)].append(word)

        # Convert the values (groups of anagrams) in the dictionary to a list and return it.
        return list(anagram_groups.values())
