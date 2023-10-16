# LeetCode Link: https://leetcode.com/problems/top-k-frequent-elements/
from collections import defaultdict


class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # Create a dictionary to count the frequency of each number.
        num_freq = defaultdict(int)
        for num in nums:
            num_freq[num] += 1

        # Create a list of lists to store numbers by their frequency.
        freq_elements = [[] for _ in range(len(nums))]

        # Group numbers by their frequency.
        for num, freq in num_freq.items():
            freq_elements[freq - 1].append(num)

        # Initialize a list to store the top k frequent elements.
        top_freq_elements = list()

        # Start from the highest frequency and add elements until reaching k.
        i = len(freq_elements) - 1
        while i >= 0 and k > 0:
            top_freq_elements.extend(freq_elements[i])
            k -= len(freq_elements[i])
            i -= 1

        return top_freq_elements
