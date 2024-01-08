# LeetCode Link: https://leetcode.com/problems/spiral-matrix/
class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        # Initialize an empty list to store the elements in spiral order
        spiral = list()

        # Initialize pointers for the boundaries of the matrix
        top, bottom, left, right = 0, len(matrix), 0, len(matrix[0])

        # Traverse the matrix in a spiral order
        while left < right and top < bottom:
            # Move from left to right
            for i in range(left, right):
                spiral.append(matrix[top][i])
            top += 1

            # Move from top to bottom
            for i in range(top, bottom):
                spiral.append(matrix[i][right - 1])
            right -= 1

            # Check if there are still elements to process
            if not (left < right and top < bottom):
                break

            # Move from right to left
            for i in range(right - 1, left - 1, -1):
                spiral.append(matrix[bottom - 1][i])
            bottom -= 1

            # Move from bottom to top
            for i in range(bottom - 1, top - 1, -1):
                spiral.append(matrix[i][left])
            left += 1

        # Return the final list in spiral order
        return spiral
