# LeetCode Link: https://leetcode.com/problems/surrounded-regions/
class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        ROWS = len(board)
        COLS = len(board[0])

        def isValid(i, j):
            # Check if the cell is within the boundaries of the board and contains "O"
            return 0 <= i < ROWS and 0 <= j < COLS and board[i][j] == "O"

        def dfs(i, j):
            # Depth-first search to mark connected "O" cells as "T"
            if not isValid(i, j):
                return
            board[i][j] = "T"  # Mark the current cell as "T"
            directions = [
                (0, 1),
                (0, -1),
                (1, 0),
                (-1, 0),
            ]  # Possible directions to move
            for direction in directions:
                row_move, col_move = direction
                next_row, next_col = i + row_move, j + col_move
                dfs(next_row, next_col)  # Recursively explore neighboring cells

        # Starting from the borders - reverse checking
        for i in range(ROWS):
            dfs(i, 0)  # Check left border
            dfs(i, COLS - 1)  # Check right border

        for j in range(COLS):
            dfs(0, j)  # Check top border
            dfs(ROWS - 1, j)  # Check bottom border

        # Checking through the board
        for i in range(ROWS):
            for j in range(COLS):
                if board[i][j] == "O":
                    board[i][j] = "X"  # Flip "O" to "X" if it is not surrounded by "X"
                elif board[i][j] == "T":
                    board[i][j] = "O"  # Restore temporarily marked "T" cells to "O"
