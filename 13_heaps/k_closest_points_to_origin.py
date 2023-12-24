# LeetCode Link: https://leetcode.com/problems/k-closest-points-to-origin/
import heapq


class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        # Initialize a list to act as a min-heap
        heap = list()

        # Calculate the distance for each point, convert to a tuple (distance, [x, y]), and push into the heap
        for point in points:
            x, y = point
            dist = sqrt(x**2 + y**2)
            heap.append((dist, [x, y]))

        # Heapify the list to maintain the min-heap property
        heapq.heapify(heap)

        # Extract the k closest points from the heap
        closest_points = list()
        for _ in range(k):
            dist, point = heapq.heappop(heap)
            closest_points.append(point)

        # Return the k closest points
        return closest_points
