# Leetcode Link: https://leetcode.com/problems/top-k-frequent-elements/
from collections import defaultdict


class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        num_freq = defaultdict(int)
        for num in nums:
            num_freq[num] += 1
        freq_elements = [[] for _ in range(len(nums))]
        for num, freq in num_freq.items():
            freq_elements[freq - 1].append(num)
        print(freq_elements)
        top_freq_elements = list()
        i = len(freq_elements) - 1
        while i >= 0 and k > 0:
            top_freq_elements.extend(freq_elements[i])
            k -= len(freq_elements[i])
            i -= 1
        return top_freq_elements
