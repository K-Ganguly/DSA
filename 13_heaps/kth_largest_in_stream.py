# LeetCode Link: https://leetcode.com/problems/kth-largest-element-in-a-stream/description/
import heapq


class KthLargest:
    def __init__(self, k: int, nums: List[int]):
        # Initialize the object with a heapified list of numbers
        heapq.heapify(nums)
        self.heap = nums
        self.k = k

        # Ensure the heap contains only the k largest elements
        while len(self.heap) > self.k:
            heapq.heappop(self.heap)

    def add(self, val: int) -> int:
        # If the heap size is less than k, add the value directly
        if len(self.heap) < self.k:
            heapq.heappush(self.heap, val)
        else:
            # If the heap is full, push the new value and pop the smallest element
            heapq.heappushpop(self.heap, val)

        # Return the kth largest element, which is the smallest element in the heap
        return self.heap[0]


# Your KthLargest object will be instantiated and called as such:
# obj = KthLargest(k, nums)
# param_1 = obj.add(val)
