# LeetCode Link: https://leetcode.com/problems/jump-game/
class Solution:
    def canJump(self, nums: List[int]) -> bool:
        # Initialize the starting position and goal to the last index in the array
        start = len(nums) - 1
        goal = start

        # Iterate backward through the array
        for i in range(start, -1, -1):
            # Check if the current position, along with the maximum jump from there,
            # can reach or exceed the current goal
            if i + nums[i] >= goal:
                # If true, update the goal to the current position
                goal = i

        # If the final goal is at the beginning (index 0), it means we can reach the end
        return True if goal == 0 else False
