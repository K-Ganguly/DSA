# LeetCode Link: https://leetcode.com/problems/rotate-image/description/
class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        N = len(matrix)
        left, right = 0, N - 1
        while left < right:
            top, bottom = left, right  # as matrix is square

            # Iterate over each element in the current layer
            for i in range(right - left):
                # Store the top-left element of the current layer
                top_left = matrix[top][left + i]

                # Move bottom-left element to top-left
                matrix[top][left + i] = matrix[bottom - i][left]

                # Move bottom-right element to bottom-left
                matrix[bottom - i][left] = matrix[bottom][right - i]

                # Move top-right element to bottom-right
                matrix[bottom][right - i] = matrix[top + i][right]

                # Move top-left element (stored earlier) to top-right
                matrix[top + i][right] = top_left

            # Move to the next layer
            left += 1
            right -= 1
