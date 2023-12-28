# LeetCode Link: https://leetcode.com/problems/jump-game-ii/
class Solution:
    def jump(self, nums: List[int]) -> int:
        # Initialize the left and right pointers, and the number of jumps
        l, r = 0, 0
        num_jumps = 0

        # Continue jumping until the right pointer reaches the last index
        while r < len(nums) - 1:
            # Initialize the farthest reachable position from the current range
            farthest = 0

            # Iterate through the current range to find the farthest reachable position
            for i in range(l, r + 1):
                farthest = max(farthest, i + nums[i])

            # Move the left pointer to the position after the current range
            l = r + 1

            # Update the right pointer to the farthest reachable position in the new range
            r = farthest

            # Increment the number of jumps
            num_jumps += 1

        # Return the total number of jumps needed to reach the end
        return num_jumps
