# Approach 1: Recursion + Memoization


class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        # Length of the input array
        n = len(nums)

        # Memoization array to store calculated results
        LIS = [-1] * n

        # Recursive function to find the length of LIS starting from index i
        def getLIS(i):
            nonlocal LIS

            # If LIS for index i is already calculated, return the result
            if LIS[i] != -1:
                return LIS[i]

            # Initialize the length of LIS for the current index
            len_lis = 1

            # Iterate over indices to find the maximum LIS
            for j in range(i + 1, n):
                # If the current element is greater, update the length of LIS
                if nums[j] > nums[i]:
                    len_lis = max(len_lis, 1 + getLIS(j))

            # Memoize the result and return the length of LIS
            LIS[i] = len_lis
            return len_lis

        # Iterate through all indices and find the maximum LIS
        max_lis = 0
        for i in range(n - 1, -1, -1):
            max_lis = max(max_lis, getLIS(i))

        # Return the maximum length of LIS
        return max_lis


# Approach 2: DP


class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        # Length of the input array
        n = len(nums)

        # Array to store the length of LIS ending at each index
        LIS = [1] * n

        # Variable to store the maximum length of LIS
        max_lis = 0

        # Iterate through indices in reverse order
        for i in range(n - 1, -1, -1):
            # Iterate over indices from i to n
            for j in range(i, n):
                # If the current element is greater, update the length of LIS
                if nums[j] > nums[i]:
                    LIS[i] = max(LIS[i], 1 + LIS[j])

            # Update the maximum length of LIS
            max_lis = max(max_lis, LIS[i])

        # Return the maximum length of LIS
        return max_lis
