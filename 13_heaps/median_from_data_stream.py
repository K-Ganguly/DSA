# LeetCode Link: https://leetcode.com/problems/find-median-from-data-stream/
import heapq


class MedianFinder:
    def __init__(self):
        # Initialize two heaps: min_heap for the larger half and max_heap for the smaller half
        self.min_heap = list()
        heapq.heapify(self.min_heap)

        self.max_heap = list()
        heapq.heapify(self.max_heap)

    def addNum(self, num: int) -> None:
        # Determine whether to add the number to min_heap or max_heap based on current conditions
        if self.min_heap and num > self.min_heap[0]:
            heapq.heappush(self.min_heap, num)
        else:
            heapq.heappush(self.max_heap, -1 * num)

        # Balance the heaps to ensure the difference in size is at most 1
        if (len(self.min_heap) - len(self.max_heap)) > 1:
            element = -1 * heapq.heappop(self.min_heap)
            heapq.heappush(self.max_heap, element)
        elif (len(self.max_heap) - len(self.min_heap)) > 1:
            element = -1 * heapq.heappop(self.max_heap)
            heapq.heappush(self.min_heap, element)

    def findMedian(self) -> float:
        # Determine the median based on the sizes of min_heap and max_heap
        if len(self.min_heap) == len(self.max_heap):
            median = (self.min_heap[0] + (-1 * self.max_heap[0])) / 2.0
        elif len(self.min_heap) > len(self.max_heap):
            median = float(self.min_heap[0])
        else:
            median = float(-1 * self.max_heap[0])
        return median


# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()
