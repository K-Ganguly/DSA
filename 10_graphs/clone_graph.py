# LeetCode Link: https://leetcode.com/problems/clone-graph/
"""
# Definition for a Node.
class Node:
    def __init__(self, val=0, neighbors=None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

from typing import Optional


class Solution:
    def cloneGraph(self, node: Optional["Node"]) -> Optional["Node"]:
        # Dictionary to map old nodes to their corresponding new nodes
        old_to_new = dict()

        def dfs(node):
            # If the node has already been visited, return its corresponding new node
            if node in old_to_new:
                return old_to_new[node]

            # Create a new node with the same value as the original node
            copy = Node(node.val)

            # Map the old node to the new node in the dictionary
            old_to_new[node] = copy

            # Recursively clone the neighbors of the original node
            for neighbor in node.neighbors:
                copy.neighbors.append(dfs(neighbor))

            # Return the cloned node
            return copy

        # Start the depth-first search from the input node
        return dfs(node) if node else None
