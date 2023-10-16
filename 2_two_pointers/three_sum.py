# LeetCode Link: https://leetcode.com/problems/3sum/
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        triplets = list()
        nums.sort()  # Sort the input array for efficient processing.
        L = len(nums)
        i = 0

        while i < L:
            if nums[i] > 0:
                break

            # Skip duplicate values to avoid duplicate triplets.
            if i > 0 and nums[i] == nums[i - 1]:
                i += 1
                continue

            j = i + 1
            k = L - 1

            while j < k:
                if nums[i] + nums[j] + nums[k] == 0:
                    triplets.append([nums[i], nums[j], nums[k]])
                    j += 1
                    k -= 1

                    # Skip duplicate values for the second pointer.
                    while j < k and nums[j] == nums[j - 1]:
                        j += 1
                elif nums[i] + nums[j] + nums[k] < 0:
                    j += 1  # Adjust the second pointer if the sum is too small.
                else:
                    k -= 1  # Adjust the third pointer if the sum is too large.

            i += 1  # Move the first pointer to explore the next unique value.

        return triplets  # Return the list of unique triplets that sum to 0.
