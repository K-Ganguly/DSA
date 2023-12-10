# LeetCode Link: https://leetcode.com/problems/course-schedule/description/
from collections import defaultdict


class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        # Set to keep track of visited courses during DFS
        visited = set()

        # Dictionary to represent the graph of courses and their prerequisites
        course_map = defaultdict(list)

        # Populate the graph
        for pre, post in prerequisites:
            course_map[pre].append(post)

        # Depth First Search (DFS) function to check if a cycle exists
        def dfs(course):
            # If the course is already visited, a cycle is detected
            if course in visited:
                return False

            # If the course has no prerequisites, it can be completed
            if len(course_map[course]) == 0:
                return True

            # Mark the current course as visited
            visited.add(course)

            # Recursively check prerequisites of the current course
            for pre in course_map[course]:
                if not dfs(pre):
                    return False

            # Reset the prerequisites for the current course and mark it as not visited
            course_map[course] = list()
            visited.remove(course)

            # The current course can be completed
            return True

        # Iterate through all courses and check if each can be completed without a cycle
        for course in range(numCourses):
            if not dfs(course):
                return False

        # If no cycle is found for any course, all courses can be completed
        return True
