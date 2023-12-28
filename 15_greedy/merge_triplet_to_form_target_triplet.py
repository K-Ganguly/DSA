# LeetCode Link: https://leetcode.com/problems/merge-triplets-to-form-target-triplet/
class Solution:
    def mergeTriplets(self, triplets: List[List[int]], target: List[int]) -> bool:
        # Initialize a set to keep track of indices where triplets match the target
        good = set()

        # Iterate through each triplet in the given list
        for triplet in triplets:
            # Check if any element in the triplet exceeds the corresponding target element
            if (
                triplet[0] > target[0]
                or triplet[1] > target[1]
                or triplet[2] > target[2]
            ):
                # If any element exceeds the target, skip to the next triplet
                continue

            # Check each element of the triplet against the target
            for i in range(3):
                # If the current element in the triplet matches the target, mark its index as good
                if triplet[i] == target[i]:
                    good.add(i)

                    # If all three indices are marked as good, the target can be formed
                    if len(good) == 3:
                        return True

        # If no triplet is found to match the target, return False
        return False
