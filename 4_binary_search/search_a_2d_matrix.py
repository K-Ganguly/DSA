# LeetCode Link: https://leetcode.com/problems/search-a-2d-matrix/
class Solution:
    def searchMatrix(self, matrix: List[List[int], target: int) -> bool:
        # Check if the matrix is empty or has no columns; return False in that case.
        if not matrix or not matrix[0]:
            return False

        # Get the number of rows (m) and columns (n) in the 2D matrix.
        m, n = len(matrix), len(matrix[0])

        # Initialize pointers for binary search: left at the start (0) and right at the end of the 1D representation.
        left, right = 0, m * n - 1

        # Perform binary search in the range [left, right].
        while left <= right:
            # Calculate the middle index for the 1D representation.
            mid = (left + right) // 2

            # Map the 1D index (mid) back to the corresponding row and column indices.
            row, col = divmod(mid, n)

            # Check if the element at matrix[row][col] is equal to the target.
            if matrix[row][col] == target:
                return True
            # If the element is less than the target, update the left pointer to search the right half.
            elif matrix[row][col] < target:
                left = mid + 1
            # If the element is greater than the target, update the right pointer to search the left half.
            else:
                right = mid - 1

        # If the loop exits without finding the target, return False.
        return False
