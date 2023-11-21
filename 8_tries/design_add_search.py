# LeetCode Link: https://leetcode.com/problems/design-add-and-search-words-data-structure/
class TrieNode:
    def __init__(self):
        # Each TrieNode represents a character in a word
        # children is a dictionary mapping characters to their corresponding TrieNodes
        self.children = {}
        # end_of_word is a flag indicating if the node represents the end of a word
        self.end_of_word = False


class WordDictionary:
    def __init__(self):
        # The root of the Trie representing the dictionary
        self.root = TrieNode()

    def addWord(self, word: str) -> None:
        # Function to add a word to the Trie
        curr = self.root
        for ch in word:
            # Traverse the Trie, adding new nodes as needed for each character
            if ch not in curr.children:
                curr.children[ch] = TrieNode()
            curr = curr.children[ch]
        # Mark the last node as the end of the added word
        curr.end_of_word = True

    def search(self, word: str) -> bool:
        # Function to search for a word in the Trie using depth-first search
        curr = self.root

        def dfs(j, curr):
            # Traverse the Trie based on the characters in the given word
            for i in range(j, len(word)):
                ch = word[i]
                if ch == ".":
                    # If the character is '.', recursively check all child nodes
                    # for possible matches for the remaining part of the word
                    for child in curr.children.values():
                        if dfs(i + 1, child):
                            return True
                    return False
                else:
                    # If the character is not '.', check if it exists in the Trie
                    if ch not in curr.children:
                        return False
                    curr = curr.children[ch]
            # Check if the last node reached represents the end of a word
            return curr.end_of_word

        # Start the search from the root of the Trie
        return dfs(0, self.root)


# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)
