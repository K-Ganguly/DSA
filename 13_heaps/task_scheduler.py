# LeetCode Link: https://leetcode.com/problems/task-scheduler/
from collections import deque, Counter
import heapq


class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        # Create a min-heap with the negation of task frequencies
        task_heap = [-freq for freq in Counter(tasks).values()]
        heapq.heapify(task_heap)

        # Initialize a deque to handle idle time and a variable to track time
        q = deque()
        time = 0

        # Continue until both the heap and queue are empty
        while task_heap or q:
            # Increment time at the beginning of each iteration
            time += 1

            # If there are tasks in the heap
            if task_heap:
                # Pop the smallest task frequency from the heap
                task = heapq.heappop(task_heap)

                # Increment the frequency and check if it is nonzero
                task += 1
                if task:
                    # Append the task and its next available time to the queue
                    q.append((task, time + n))
            else:
                # If the heap is empty, set time to the next available time in the queue
                time = q[0][1]

            # If there are tasks in the queue and the current time matches the next available time
            if q and time == q[0][1]:
                # Pop the task from the queue and push it back to the heap
                task = q.popleft()[0]
                heapq.heappush(task_heap, task)

        # Return the total time taken to execute all tasks
        return time
