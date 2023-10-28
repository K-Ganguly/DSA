# LeetCode Link: https://leetcode.com/problems/median-of-two-sorted-arrays/
class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        # Ensure that nums1 is the smaller array to optimize the algorithm.
        if len(nums2) < len(nums1):
            nums1, nums2 = nums2, nums1
        total_len = len(nums1) + len(nums2)
        half_len = total_len // 2

        # Initialize pointers for binary search.
        left = 0
        right = len(nums1) - 1

        while True:
            # Calculate the partition points for both arrays.
            left_partition_1 = left + (right - left) // 2
            left_partition_2 = half_len - left_partition_1 - 2

            # Find the elements on the left and right sides of the partitions,
            # taking care to handle out-of-bounds conditions using -inf and +inf.
            left_element_1 = (
                nums1[left_partition_1] if left_partition_1 >= 0 else float("-inf")
            )
            left_element_2 = (
                nums2[left_partition_2] if left_partition_2 >= 0 else float("-inf")
            )
            right_element_1 = (
                nums1[left_partition_1 + 1]
                if (left_partition_1 + 1) < len(nums1)
                else float("inf")
            )
            right_element_2 = (
                nums2[left_partition_2 + 1]
                if (left_partition_2 + 1) < len(nums2)
                else float("inf")
            )

            # Check if the elements in the partitions satisfy the median condition.
            if left_element_1 <= right_element_2 and left_element_2 <= right_element_1:
                # If the total length is even, return the average of the middle elements,
                # else return the smaller of the two middle elements.
                if total_len % 2 == 0:
                    return (
                        max(left_element_1, left_element_2)
                        + min(right_element_1, right_element_2)
                    ) / 2
                else:
                    return min(right_element_1, right_element_2)

            # Adjust the pointers for binary search.
            # If left_element_1 is greater than right_element_2, move the partition in nums1 to the left.
            # Otherwise, move it to the right.
            elif left_element_1 > right_element_2:
                right = left_partition_1 - 1
            else:
                left = left_partition_1 + 1
