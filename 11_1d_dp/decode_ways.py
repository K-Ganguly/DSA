# Approach 1: Recursion with Memoization
class Solution:
    def numDecodings(self, s: str) -> int:
        n = len(s)
        decode_map = {n: 1}

        def findNumDecodings(i):
            # If the result for the current index is already memoized, return it
            if i in decode_map:
                return decode_map[i]

            # If the current digit is '0', no valid decoding is possible
            if s[i] == "0":
                return 0

            # Recursively calculate the number of decodings for the current index
            decode_map[i] = findNumDecodings(i + 1)

            # Check if two digits can form a valid decoding
            if i < n - 1 and (s[i] == "1" or (s[i] == "2" and s[i + 1] in "0123456")):
                decode_map[i] += findNumDecodings(i + 2)

            return decode_map[i]

        # Start the recursive calculation from the beginning of the string
        return findNumDecodings(0)


# Approach 2: DP-Basic
class Solution:
    def numDecodings(self, s: str) -> int:
        n = len(s)

        # Initialize an array to store the number of decodings for each index
        decode_map = [0] * (n + 1)
        decode_map[n] = 1  # There is one way to decode an empty string
        decode_map[n - 1] = 1  # There is one way to decode a string with a single digit

        # Iterate through the string from right to left
        for i in range(n - 1, -1, -1):
            # If the current digit is '0', no valid decoding is possible
            if s[i] == "0":
                decode_map[i] = 0
            else:
                # The number of decodings for the current index is initially the same as the next index
                decode_map[i] = decode_map[i + 1]

            # Check if two digits can form a valid decoding
            if (i < n - 1) and (s[i] == "1" or (s[i] == "2" and s[i + 1] in "0123456")):
                decode_map[i] += decode_map[i + 2]

        # The final result is stored at the beginning of the array
        return decode_map[0]


# Approach 3: DP-Space Optimized
class Solution:
    def numDecodings(self, s: str) -> int:
        n = len(s)

        # Initialize variables to optimize space usage
        res = 0
        one = 1
        two = 0

        # Iterate through the string from right to left
        for i in range(n - 1, -1, -1):
            # If the current digit is '0', no valid decoding is possible
            if s[i] == "0":
                res = 0
            else:
                # The result is initially set to the value of 'one'
                res = one

            # Check if two digits can form a valid decoding
            if (i < n - 1) and (s[i] == "1" or (s[i] == "2" and s[i + 1] in "0123456")):
                res += two

            # Swap variables to maintain the necessary state
            temp = one
            one = res
            two = temp

        # The final result is stored in 'res'
        return res
