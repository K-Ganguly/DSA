# LeetCode Link: https://leetcode.com/problems/partition-labels/
class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        # Create a dictionary to store the last index of each character in the string
        ch_last_idx = dict()
        for i, ch in enumerate(s):
            ch_last_idx[ch] = i

        # Initialize variables to track the end index, length of the current partition, and the list of partitions
        end = 0
        len_partition = 0
        partitions = list()

        # Iterate through each character and its index in the string
        for i, ch in enumerate(s):
            # Increment the length of the current partition
            len_partition += 1

            # Update the end index to the maximum of its current value and the last index of the current character
            end = max(end, ch_last_idx[ch])

            # If the current index is equal to the updated end index, it marks the end of the current partition
            if i == end:
                # Add the length of the current partition to the list of partitions
                partitions.append(len_partition)

                # Reset the length of the current partition to 0 for the next iteration
                len_partition = 0

        # Return the list of partition lengths
        return partitions
