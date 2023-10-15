# Leetcode Link: https://leetcode.com/problems/valid-sudoku/
class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        row = [set() for _ in range(9)]
        col = [set() for _ in range(9)]
        block = [set() for _ in range(9)]

        for i in range(len(board)):
            for j in range(len(board[0])):
                element = board[i][j]
                block_idx = ((i // 3) * 3) + j // 3
                if element == ".":
                    continue
                elif (
                    (element in row[i])
                    or (element in col[j])
                    or (element in block[block_idx])
                ):
                    return False
                else:
                    row[i].add(element)
                    col[j].add(element)
                    block[block_idx].add(element)

        return True
