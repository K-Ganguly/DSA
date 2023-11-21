# LeetCode Link: https://leetcode.com/problems/combination-sum/
class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        combinations = []

        def check_combination(start, remaining_target, current_combination):
            if remaining_target == 0:
                # If the target is achieved, add the current combination to the list
                combinations.append(current_combination.copy())
                return

            if remaining_target < 0 or start >= len(candidates):
                # If the target is exceeded or all candidates are exhausted, stop recursion
                return

            for i in range(start, len(candidates)):
                num = candidates[i]
                current_combination.append(num)
                check_combination(i, remaining_target - num, current_combination)
                current_combination.pop()

        check_combination(0, target, [])
        return combinations
