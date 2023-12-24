# LeetCode Link: https://leetcode.com/problems/kth-largest-element-in-an-array/
import heapq


class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        # Initialize an empty list 'heap' to act as a min-heap
        heap = list()

        # Convert the list 'heap' into a min-heap
        heapq.heapify(heap)

        # Iterate through each element in the input list 'nums'
        for num in nums:
            # Push the current element onto the min-heap
            heapq.heappush(heap, num)

            # If the size of the min-heap exceeds k, remove the smallest element
            if len(heap) > k:
                heapq.heappop(heap)

        # The top of the min-heap now contains the kth largest element
        return heap[0]
