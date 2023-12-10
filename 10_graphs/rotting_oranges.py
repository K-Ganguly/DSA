# LeetCode Link: https://leetcode.com/problems/rotting-oranges/description/
from collections import deque


class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        # Get the number of rows and columns in the grid
        ROWS = len(grid)
        COLS = len(grid[0])

        # Initialize variables to count fresh oranges and store the positions of rotten oranges
        num_fresh_oranges = 0
        rotten_oranges = deque()

        # Iterate through the grid to count fresh oranges and find initial rotten oranges
        for i in range(ROWS):
            for j in range(COLS):
                if grid[i][j] == 1:
                    num_fresh_oranges += 1
                elif grid[i][j] == 2:
                    rotten_oranges.append((i, j))

        # Function to check if a given position is a valid, fresh orange
        def isValid(i, j):
            return 0 <= i < ROWS and 0 <= j < COLS and grid[i][j] == 1

        # Initialize time variable to track the minutes passed
        time = 0

        # Perform BFS to simulate the rotting process
        while num_fresh_oranges > 0 and rotten_oranges:
            length = len(rotten_oranges)
            for k in range(length):
                i, j = rotten_oranges.popleft()
                directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
                for direction in directions:
                    row_move, col_move = direction
                    r = i + row_move
                    c = j + col_move
                    if isValid(r, c):
                        # Mark the fresh orange as rotten and update counts
                        grid[r][c] = 2
                        num_fresh_oranges -= 1
                        rotten_oranges.append((r, c))

            # Increment time after processing each minute
            time += 1

        # If there are no more fresh oranges, return the time taken; otherwise, return -1
        return time if num_fresh_oranges == 0 else -1
