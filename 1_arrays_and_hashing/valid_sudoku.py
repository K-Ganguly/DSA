# LeetCode Link: https://leetcode.com/problems/valid-sudoku/
class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        # Initialize sets to track unique values in each row, column, and block.
        row = [set() for _ in range(9)]
        col = [set() for _ in range(9)]
        block = [set() for _ in range(9)]

        for i in range(len(board)):
            for j in range(len(board[0])):
                element = board[i][j]
                block_idx = ((i // 3) * 3) + j // 3

                # If the element is '.', continue as it doesn't affect the validity.
                if element == ".":
                    continue
                # Check if the element is already present in the row, column, or block.
                elif (
                    (element in row[i])
                    or (element in col[j])
                    or (element in block[block_idx])
                ):
                    return False
                # If the element is unique, add it to the respective sets.
                else:
                    row[i].add(element)
                    col[j].add(element)
                    block[block_idx].add(element)

        return True
