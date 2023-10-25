# LeetCode Link: https://leetcode.com/problems/largest-rectangle-in-histogram/submissions/1083925861/
class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        # Initialize a stack to keep track of indices of the histogram bars.
        stack = list()
        # Initialize the maximum area as 0.
        max_area = 0

        # Iterate through each histogram bar and its index.
        for i, ht in enumerate(heights):
            # While the stack is not empty and the current bar's height is less than the height of the bar at the top of the stack:
            while stack and heights[stack[-1]] > ht:
                # Pop the top of the stack and use its height.
                height = heights[stack.pop()]
                # Calculate the width of the rectangle as the difference between the current index 'i' and the index at the top of the stack.
                # If the stack is empty, the width is just 'i' (no previous bar to the left).
                width = (i - stack[-1] - 1) if stack else i
                # Calculate the area of the current rectangle.
                curr_area = height * width
                # Update the maximum area.
                max_area = max(curr_area, max_area)

            # Push the current index onto the stack.
            stack.append(i)

        # After processing all bars in the histogram, there might be some remaining bars in the stack.
        while stack:
            # Pop a bar's height from the stack.
            height = heights[stack.pop()]
            # Calculate the width of the rectangle similarly to the previous loop.
            width = (len(heights) - stack[-1] - 1) if stack else len(heights)
            # Calculate the area of the current rectangle.
            curr_area = height * width
            # Update the maximum area.
            max_area = max(curr_area, max_area)

        # Return the maximum area of the largest rectangle.
        return max_area
