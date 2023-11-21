class TrieNode:
    def __init__(self):
        # Each TrieNode has a dictionary 'children' to store the next level of characters
        self.children = {}
        # 'end_of_word' indicates whether the current node represents the end of a word
        self.end_of_word = False


class Trie:
    def __init__(self):
        # Initialize the Trie with a root node
        self.root = TrieNode()

    def insert(self, word: str) -> None:
        # Start from the root
        curr = self.root
        # Traverse through each character in the word
        for ch in word:
            # If the character is not in the current node's children, add a new TrieNode
            if ch not in curr.children:
                curr.children[ch] = TrieNode()
            # Move to the next level of the Trie
            curr = curr.children[ch]
        # Mark the end of the word in the last TrieNode
        curr.end_of_word = True

    def search(self, word: str) -> bool:
        # Start from the root
        curr = self.root
        # Traverse through each character in the word
        for ch in word:
            # If the character is not in the current node's children, the word is not present
            if ch not in curr.children:
                return False
            # Move to the next level of the Trie
            curr = curr.children[ch]
        # Check if the last TrieNode marks the end of a word
        return curr.end_of_word

    def startsWith(self, prefix: str) -> bool:
        # Start from the root
        curr = self.root
        # Traverse through each character in the prefix
        for ch in prefix:
            # If the character is not in the current node's children, the prefix is not present
            if ch not in curr.children:
                return False
            # Move to the next level of the Trie
            curr = curr.children[ch]
        # The prefix is present in the Trie
        return True
