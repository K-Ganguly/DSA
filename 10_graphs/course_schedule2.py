# LeetCode Link: https://leetcode.com/problems/course-schedule-ii/
from collections import defaultdict
from typing import List


class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        # List to store the final ordering of courses
        routine = list()

        # Set to keep track of visited courses during DFS
        visited = set()

        # Set to detect cycles during DFS
        cycle = set()

        # Dictionary to represent the graph of courses and their prerequisites
        course_map = defaultdict(list)

        # Populate the graph
        for pre, post in prerequisites:
            course_map[pre].append(post)

        # Depth First Search (DFS) function to find the course ordering
        def dfs(course):
            # If the course is already part of a cycle, return False
            if course in cycle:
                return False

            # If the course has already been visited, return True
            if course in visited:
                return True

            # Mark the current course as part of the cycle
            cycle.add(course)

            # Recursively check prerequisites of the current course
            for pre in course_map[course]:
                if not dfs(pre):
                    return False

            # Remove the current course from the cycle set
            cycle.remove(course)

            # Mark the current course as visited
            visited.add(course)

            # Append the current course to the final ordering
            routine.append(course)

            # Return True to indicate successful traversal
            return True

        # Iterate through all courses and check if each can be completed without a cycle
        for course in range(numCourses):
            if not dfs(course):
                # If a cycle is found, return an empty list indicating no valid ordering
                return []

        # If no cycle is found for any course, return the final ordering
        return routine
