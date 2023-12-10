# LeetCode Link: https://leetcode.com/problems/max-area-of-island/
class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        # Set to keep track of visited cells
        visited = set()
        # Variable to store the size of the biggest island
        biggest_island = 0

        # Function to check if a cell is valid for exploration
        def isValid(i, j):
            # Check if the cell is within the grid bounds, has a value of 1, and has not been visited
            return (
                0 <= i < len(grid)
                and 0 <= j < len(grid[0])
                and grid[i][j] == 1
                and (i, j) not in visited
            )

        # Depth-first search function to explore the island and calculate its size
        def dfs(i, j):
            # If the cell is not valid, return 0
            if not isValid(i, j):
                return 0
            # Initialize the island size to 1 for the current cell
            curr_island = 1
            # Mark the cell as visited
            visited.add((i, j))
            # Define possible directions to explore: right, down, up, left
            directions = [(0, 1), (1, 0), (-1, 0), (0, -1)]
            # Explore each direction recursively
            for direction in directions:
                row_move, col_move = direction
                curr_island += dfs(i + row_move, j + col_move)
            # Return the total size of the island
            return curr_island

        # Iterate through each cell in the grid
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                # Check if the cell is valid for exploration
                if isValid(i, j):
                    # Perform DFS to calculate the size of the current island
                    curr_island_area = dfs(i, j)
                    # Update the biggest island size if the current island is larger
                    biggest_island = max(curr_island_area, biggest_island)

        # Return the size of the biggest island
        return biggest_island
