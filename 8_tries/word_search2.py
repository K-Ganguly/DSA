# LeetCode Link: https://leetcode.com/problems/word-search-ii/
class TrieNode:
    def __init__(self):
        # Each TrieNode has a dictionary to store its children (next characters)
        self.children = dict()
        # Flag to indicate whether the current TrieNode represents the end of a word
        self.end_of_word = False

    def add_word(self, word):
        # Add a word to the Trie by traversing the TrieNodes for each character
        curr = self
        for ch in word:
            # If the character is not in the children, create a new TrieNode
            if ch not in curr.children:
                curr.children[ch] = TrieNode()
            # Move to the next TrieNode
            curr = curr.children[ch]
        # Mark the last TrieNode as the end of the word
        curr.end_of_word = True


class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        # Create the Trie and add all the words to it
        root = TrieNode()
        for word in words:
            root.add_word(word)

        # Initialize a set to store unique found words during DFS
        res = set()
        ROWS = len(board)
        COLS = len(board[0])

        def dfs(i, j, node, word):
            # Base cases for DFS termination
            if (
                i < 0
                or i >= ROWS
                or j < 0
                or j >= COLS
                or board[i][j] == "/"
                or board[i][j] not in node.children
            ):
                return

            # Append the current character to the word being formed
            word += board[i][j]
            # Check if the current TrieNode represents the end of a word
            if node.children[board[i][j]].end_of_word:
                # Add the word to the result set
                res.add(word)

            # Move to the next TrieNode and mark the current cell as visited
            node = node.children[board[i][j]]
            temp = board[i][j]
            board[i][j] = "/"

            # Explore in all four directions (up, down, left, right) using DFS
            directions = ((0, 1), (0, -1), (1, 0), (-1, 0))
            for direction in directions:
                row_move, col_move = direction
                dfs(i + row_move, j + col_move, node, word)

            # Backtrack by restoring the original character in the current cell
            board[i][j] = temp

        # Start DFS from each cell in the board
        for i in range(ROWS):
            for j in range(COLS):
                dfs(i, j, root, "")

        # Convert the set of unique words to a list and return
        return list(res)
