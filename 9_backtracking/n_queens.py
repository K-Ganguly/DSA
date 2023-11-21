# LeetCode Link: https://leetcode.com/problems/n-queens/
class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        # Sets to keep track of occupied columns and diagonals
        col_placement = set()  # Set of occupied columns
        pos_diagonal = set()  # Set of occupied positive diagonals (r + c)
        neg_diagonal = set()  # Set of occupied negative diagonals (r - c)

        # Initialize the chessboard with empty cells
        board = [["."] * n for _ in range(n)]
        arrangements = list()

        # Function to recursively place queens on the board
        def placeQueen(r):
            # If all queens are placed successfully, add the current board configuration to the result
            if r == n:
                board_placement = ["".join(row) for row in board]
                arrangements.append(board_placement)
                return

            # Try placing the queen in each column of the current row
            for c in range(n):
                # Check if the current position conflicts with existing queens
                if (
                    c in col_placement
                    or (r + c) in pos_diagonal
                    or (r - c) in neg_diagonal
                ):
                    continue

                # Place the queen and update sets to mark occupied positions
                board[r][c] = "Q"
                col_placement.add(c)
                pos_diagonal.add(r + c)
                neg_diagonal.add(r - c)

                # Recursively try placing queens in the next row
                placeQueen(r + 1)

                # Backtrack: Undo the placement and remove the queen from the sets
                board[r][c] = "."
                col_placement.remove(c)
                pos_diagonal.remove(r + c)
                neg_diagonal.remove(r - c)

        # Start the placement process from the first row
        placeQueen(0)

        return arrangements
