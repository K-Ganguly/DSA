# LeetCode Link: https://leetcode.com/problems/set-matrix-zeroes/
class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        # Initialize flags to track if the first row and column contain zeros
        first_col_zero = False
        first_row_zero = False

        # Get the dimensions of the matrix
        M = len(matrix)
        N = len(matrix[0])

        # Check if the first row contains any zeros
        for j in range(N):
            if matrix[0][j] == 0:
                first_row_zero = True
                break

        # Check if the first column contains any zeros
        for i in range(M):
            if matrix[i][0] == 0:
                first_col_zero = True
                break

        # Iterate through the matrix, marking the first element of the row and column
        # as zero if the corresponding element in that row or column is zero
        for i in range(1, M):
            for j in range(1, N):
                if matrix[i][j] == 0:
                    matrix[i][0] = 0
                    matrix[0][j] = 0

        # Iterate through the matrix again, setting the entire row or column to zero
        # if the first element of that row or column is marked as zero
        for i in range(1, M):
            for j in range(1, N):
                if matrix[i][0] == 0 or matrix[0][j] == 0:
                    matrix[i][j] = 0

        # If the first row originally contained a zero, set all elements in the first row to zero
        if first_row_zero:
            for j in range(N):
                matrix[0][j] = 0

        # If the first column originally contained a zero, set all elements in the first column to zero
        if first_col_zero:
            for i in range(M):
                matrix[i][0] = 0
