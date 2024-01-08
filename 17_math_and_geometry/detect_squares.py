# LeetCode Link: https://leetcode.com/problems/detect-squares/
from collections import defaultdict


class DetectSquares:
    def __init__(self):
        # Initialize a defaultdict to store the counts of each point
        self.point_counts = defaultdict(int)

        # Initialize a list to store all points added to the system
        self.points = list()

    def add(self, point: List[int]) -> None:
        # Increment the count of the given point and add it to the list of points
        self.point_counts[tuple(point)] += 1
        self.points.append(tuple(point))

    def count(self, point: List[int]) -> int:
        # Initialize a variable to store the number of squares containing the given point
        num_squares = 0

        # Extract x and y coordinates from the input point
        x, y = point

        # Iterate through all points in the system
        for point_1 in self.points:
            # Extract x and y coordinates of the current point in the iteration
            px, py = point_1

            # Check if the current point, along with the input point, forms a square
            if abs(px - x) == abs(py - y) and px != x and py != y:
                # If the condition is met, calculate the number of squares
                num_squares += self.point_counts[(x, py)] * self.point_counts[(px, y)]

        # Return the total number of squares containing the given point
        return num_squares


# Your DetectSquares object will be instantiated and called as such:
# obj = DetectSquares()
# obj.add(point)
# param_2 = obj.count(point)
