# Leetcode Link: https://leetcode.com/problems/trapping-rain-water/
class Solution:
    def trap(self, height: List[int]) -> int:
        # Initialize two pointers at the left and right ends of the array.
        left = 0
        right = len(height) - 1

        # Initialize variables to keep track of the maximum heights on the left and right sides,
        # and the total trapped water.
        maxLeft = 0
        maxRight = 0
        totalWaterContained = 0

        # Continue until the left and right pointers meet or cross each other.
        while left <= right:
            # Initialize the variable to track water contained at the current position.
            waterContained = 0

            # We check whether the current left side is lower or equal to the current right side.
            if maxLeft <= maxRight:
                # If the height at the left pointer is greater than or equal to maxLeft,
                # it means the current left wall can contain more water if there's a taller wall to the right.
                # Therefore, we update maxLeft to track the highest wall to the left.
                if height[left] >= maxLeft:
                    maxLeft = max(height[left], maxLeft)
                else:
                    # If the height at the left pointer is lower than maxLeft, it means there's a potential
                    # space for water to be trapped. We calculate the water height and add it to the total water contained.
                    waterContained = maxLeft - height[left]
                # Move the left pointer to the right, indicating that we've processed this position.
                left += 1
            else:
                # Similarly, we check the right side.
                if height[right] >= maxRight:
                    # If the height at the right pointer is greater than or equal to maxRight,
                    # we update maxRight to track the highest wall to the right.
                    maxRight = max(height[right], maxRight)
                else:
                    # If the height at the right pointer is lower than maxRight, it means there's potential
                    # space for water to be trapped. We calculate the water height and add it to the total water contained.
                    waterContained = maxRight - height[right]
                # Move the right pointer to the left, indicating that we've processed this position.
                right -= 1

            # Add the water contained at the current position to the total water contained.
            totalWaterContained += waterContained

        # Return the total trapped water at the end.
        return totalWaterContained
