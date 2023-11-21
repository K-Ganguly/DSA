from collections import defaultdict


class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        # Use defaultdict to keep track of character frequencies in the word
        word_freq = defaultdict(int)
        # List to store the starting positions of the first character of the word
        start_pos = list()

        # Iterate through the board to populate word_freq and find starting positions
        for i, row in enumerate(board):
            for j, ch in enumerate(row):
                word_freq[ch] += 1
                if ch == word[0]:
                    start_pos.append((i, j))

        # Check if there are enough characters in the board for each character in the word
        for ch in word:
            word_freq[ch] -= 1
            if word_freq[ch] < 0:
                return False

        # Function to recursively check if the word can be formed from a given position
        def check_word(i, j, k):
            # Base cases:
            # Out of bounds check
            if (
                i >= len(board)
                or j >= len(board[0])
                or i < 0
                or j < 0
                # Character in the board does not match with the corresponding character of the word
                or board[i][j] != word[k]
                # The place is already visited
                or board[i][j] == "/"
            ):
                return False

            # If we reached the end of the word, return True
            if k == len(word) - 1:
                return True

            # Mark the current position as visited
            board[i][j], temp = "/", board[i][j]

            # Explore in all directions (up, down, left, right)
            directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
            for direction in directions:
                row_move, col_move = direction
                next_row, next_col = i + row_move, j + col_move
                # If the recursive call returns True, return True
                if check_word(next_row, next_col, k + 1):
                    return True

            # Backtrack: restore the original character at the current position
            board[i][j] = temp

            return False

        # Check if the word can be formed from any of the starting positions
        for pos in start_pos:
            i, j = pos[0], pos[1]
            if check_word(i, j, 0):
                return True

        # If no valid path is found, return False
        return False
