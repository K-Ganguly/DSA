# Leetcode Link: https://leetcode.com/problems/longest-consecutive-sequence/
class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums_set = set(nums)
        max_seq_len = 0
        for num in nums_set:
            seq_len = 0
            prev_num = num - 1
            if prev_num not in nums_set:
                curr_num = num
                while curr_num in nums_set:
                    seq_len += 1
                    curr_num += 1
            max_seq_len = max(seq_len, max_seq_len)
        return max_seq_len
