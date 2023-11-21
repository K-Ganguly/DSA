# LeetCode Link: https://leetcode.com/problems/palindrome-partitioning/
class Solution:
    def partition(self, s: str) -> List[List[str]]:
        # Initialize the result list to store all possible partitions
        res = list()

        # Initialize the current partition list
        part = list()

        # Helper function to check if a substring is a palindrome
        def isPali(left, right):
            while left <= right:
                if s[left] != s[right]:
                    return False
                left += 1
                right -= 1
            return True

        # Depth-first search function to generate all valid partitions
        def dfs(i):
            # If the current index exceeds the length of the input string,
            # the current partition is valid, so add it to the result list
            if i >= len(s):
                res.append(part.copy())
                return

            # Iterate through the string starting from the current index
            for j in range(i, len(s)):
                # Check if the substring from i to j is a palindrome
                if isPali(i, j):
                    # If it is a palindrome, add it to the current partition
                    part.append(s[i : j + 1])

                    # Recursively call the dfs function for the next index
                    dfs(j + 1)

                    # Backtrack: Remove the last added substring to explore other possibilities
                    part.pop()

        # Start the depth-first search from the beginning of the string
        dfs(0)

        # Return the list of all valid partitions
        return res
