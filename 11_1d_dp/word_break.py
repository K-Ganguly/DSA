# LeetCode Link: https://leetcode.com/problems/word-break/
# Approach 1: Recursion with Memoization
class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        n = len(s)
        break_possible = [None] * (n + 1)
        break_possible[n] = [True]

        def check_break(i):
            if break_possible[i] != None:
                return break_possible[i]

            break_check = False
            for word in wordDict:
                l = len(word)
                s2 = s[i : (i + l)]
                if s2 == word:
                    break_check = check_break(i + l)
                    if break_check:
                        break
            break_possible[i] = break_check
            return break_check

        check_break(0)
        return break_possible[0]


# Approach 2: DP-basic
class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        n = len(s)
        break_possible = [False] * (n + 1)
        break_possible[n] = True

        for i in range(n, -1, -1):
            for word in wordDict:
                l = len(word)
                if (i + l) <= n and s[i : (i + l)] == word:
                    break_check = break_possible[i + l]
                    if break_check:
                        break_possible[i] = True
                        break

        return break_possible[0]
