# LeetCode Link: https://leetcode.com/problems/word-ladder/
from collections import defaultdict, deque
from typing import List


class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        # Check if endWord is in the wordList
        if endWord not in wordList:
            return 0

        # Create a defaultdict to store words that match a certain pattern
        neighbor_list = defaultdict(list)

        # Add the beginWord to the wordList
        wordList.append(beginWord)

        # Populate neighbor_list with patterns and corresponding words
        for word in wordList:
            for i in range(0, len(word)):
                pattern = word[:i] + "*" + word[(i + 1) :]
                neighbor_list[pattern].append(word)

        # Initialize a set to keep track of visited words
        visited_words = set([beginWord])

        # Initialize a queue for BFS starting with the beginWord
        neighbor_queue = deque([beginWord])

        # Initialize the result to 1 (beginWord itself)
        res = 1

        # Perform BFS
        while neighbor_queue:
            # Get the number of elements in the current level of the queue
            len_queue = len(neighbor_queue)

            # Iterate through the current level of the queue
            for i in range(len_queue):
                # Pop a word from the queue
                word = neighbor_queue.popleft()

                # Check if the word is equal to the endWord
                if word == endWord:
                    return res

                # Generate patterns by changing one letter at a time
                for j in range(len(word)):
                    pattern = word[:j] + "*" + word[j + 1 :]

                    # Explore words that match the current pattern
                    for neighbor_word in neighbor_list[pattern]:
                        # Check if the neighbor_word has not been visited
                        if neighbor_word not in visited_words:
                            # Mark the neighbor_word as visited
                            visited_words.add(neighbor_word)

                            # Add the neighbor_word to the queue for further exploration
                            neighbor_queue.append(neighbor_word)

            # Increment the result as we move to the next level in BFS
            res += 1

        # If the endWord is not reached, return 0
        return 0
