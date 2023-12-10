# LeetCode Link: https://leetcode.com/problems/pacific-atlantic-water-flow/
class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        rows = len(heights)
        cols = len(heights[0])
        pacific = set()  # Set to store cells reachable from the Pacific Ocean
        atlantic = set()  # Set to store cells reachable from the Atlantic Ocean
        flowing_water = list()  # List to store cells reachable from both oceans

        def isValid(i, j, visited, prev_ht):
            # Helper function to check if the cell is within bounds,
            # not visited before, and has a height greater than or equal to the previous height.
            return (
                0 <= i < len(heights)
                and 0 <= j < len(heights[0])
                and (i, j) not in visited
                and heights[i][j] >= prev_ht
            )

        def dfs(i, j, visited, prev_ht):
            # Depth-first search to explore cells reachable from a given point.
            if not isValid(i, j, visited, prev_ht):
                return
            visited.add((i, j))
            directions = [
                (0, 1),
                (0, -1),
                (1, 0),
                (-1, 0),
            ]  # Possible movements: right, left, down, up
            for direction in directions:
                row_move = direction[0]
                col_move = direction[1]
                dfs(i + row_move, j + col_move, visited, heights[i][j])

        for r in range(rows):
            # Explore cells reachable from the leftmost column for both oceans
            # (Pacific Ocean for pacific set, and Atlantic Ocean for atlantic set)
            dfs(r, 0, pacific, heights[r][0])
            dfs(r, cols - 1, atlantic, heights[r][cols - 1])

        for c in range(cols):
            # Explore cells reachable from the topmost row for both oceans
            # (Pacific Ocean for pacific set, and Atlantic Ocean for atlantic set)
            dfs(0, c, pacific, heights[0][c])
            dfs(rows - 1, c, atlantic, heights[rows - 1][c])

        for i in range(rows):
            for j in range(cols):
                # Check for cells reachable from both oceans and add them to the result list.
                if (i, j) in pacific and (i, j) in atlantic:
                    flowing_water.append([i, j])

        return flowing_water
