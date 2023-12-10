# LeetCode Link: https://leetcode.com/problems/redundant-connection/
class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        # Initialize parent array with each node pointing to itself
        parent = [i for i in range(len(edges) + 1)]
        # Initialize rank array to keep track of the depth of each node in the tree
        rank = [1] * (len(edges) + 1)

        # Helper function to find the root parent of a node using path compression
        def find(n):
            p = parent[n]
            while p != parent[p]:
                parent[p] = parent[
                    parent[p]
                ]  # Path compression to make the tree more flat
                p = parent[p]
            return p

        # Helper function to perform union of two sets using rank to optimize the tree structure
        def union(n1, n2):
            par_1 = find(n1)
            par_2 = find(n2)
            if par_1 == par_2:
                return False  # Nodes are already in the same set, adding this edge creates a cycle
            if rank[par_1] >= rank[par_2]:
                rank[par_1] += 1
                parent[
                    par_2
                ] = par_1  # Attach smaller rank tree under the root of the larger rank tree
            else:
                rank[par_2] += 1
                parent[
                    par_1
                ] = par_2  # Attach smaller rank tree under the root of the larger rank tree
            return True

        # Iterate through each edge and perform union operation
        for n1, n2 in edges:
            if not union(n1, n2):
                return [
                    n1,
                    n2,
                ]  # If union fails, it means adding this edge creates a cycle, so return it as redundant
