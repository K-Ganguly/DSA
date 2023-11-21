# LeetCode Link: https://leetcode.com/problems/combination-sum-ii/
class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        # Initialize a list to store the final combinations
        combinations = list()

        # Sort the candidates to handle duplicates efficiently
        candidates.sort()

        # Helper function to explore combinations using backtracking
        def checkCombination(i, target, curr_combination):
            # If the target is 0, a valid combination is found, append it to the list
            if target == 0:
                combinations.append(curr_combination.copy())
                return

            # Base cases:
            # If we've reached the end of candidates or target becomes negative, return
            if i == len(candidates) or target < 0:
                return

            # Include the current candidate in the combination
            curr_combination.append(candidates[i])

            # Recursively explore combinations with the current candidate
            checkCombination(i + 1, target - candidates[i], curr_combination)

            # Exclude the current candidate to explore other possibilities
            curr_combination.pop()

            # Skip duplicates to avoid redundant combinations
            while i < len(candidates) - 1 and candidates[i] == candidates[i + 1]:
                i += 1

            # Continue exploring combinations with the next candidate
            checkCombination(i + 1, target, curr_combination)

        # Start the exploration from the beginning of the candidates list
        checkCombination(0, target, [])

        # Return the final list of combinations
        return combinations
