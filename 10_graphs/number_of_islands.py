# LeetCode Link: https://leetcode.com/problems/number-of-islands/
class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        num_islands = 0
        visited = set()

        # Helper function to check if a position is not valid for DFS
        def isNotValid(i, j):
            return (
                not (0 <= i < len(grid))
                or not (0 <= j < len(grid[0]))
                or grid[i][j] == "0"
                or (i, j) in visited
            )

        # Depth First Search (DFS) function to explore the island
        def dfs(i, j):
            if isNotValid(i, j):
                return

            visited.add((i, j))  # Mark the current cell as visited

            directions = [(0, 1), (1, 0), (-1, 0), (0, -1)]
            for direction in directions:
                row_move, col_move = direction
                new_i, new_j = i + row_move, j + col_move
                dfs(new_i, new_j)  # Recursively explore adjacent cells

            return

        # Main loop to iterate through each cell in the grid
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                # Check if the current cell is not part of an island
                if not isNotValid(i, j):
                    num_islands += 1  # Increment the count of islands
                    dfs(i, j)  # Start DFS to explore the current island

        return num_islands
