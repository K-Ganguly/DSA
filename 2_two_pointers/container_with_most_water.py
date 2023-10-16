# LeetCode Link: https://leetcode.com/problems/container-with-most-water/
class Solution:
    def maxArea(self, height: List[int]) -> int:
        waterContained = 0
        maxWaterContained = 0
        l = 0
        r = len(height) - 1

        while l < r:
            # Calculate the water contained by the current container.
            waterContained = min(height[l], height[r]) * abs(l - r)
            maxWaterContained = max(waterContained, maxWaterContained)

            # Move the pointers towards each other to potentially find a greater container.
            if height[l] >= height[r]:
                r -= 1
            else:
                l += 1

        return maxWaterContained
