# LeetCode Link: https://leetcode.com/problems/contains-duplicate/
class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        # Create an empty set to store unique numbers encountered.
        nums_set = set()

        # Iterate through the given list of numbers.
        for num in nums:
            # Check if the current number is already in the set.
            if num in nums_set:
                # If the number is found in the set, it means we have encountered a duplicate.
                # Return True to indicate that the list contains at least one duplicate.
                return True

            # If the number is not in the set, add it to the set to keep track of unique numbers.
            nums_set.add(num)

        # If the loop completes without finding any duplicates, return False to indicate
        # that there are no duplicates in the list.
        return False
