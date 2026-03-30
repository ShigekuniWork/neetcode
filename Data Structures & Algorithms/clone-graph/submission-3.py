"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        """
        I'd approach to solve this problem by using DFS.
        I'll use a hash map to track visited nodes and prevent duplicated deep copies.
        For each node, I'll create a copy and recursively clone its neighbors.
        """
        # Initialize visited node map
        visited = {}

        # Declare dfs function
        def dfs(node):
            # When current node is in visited, return the visited node
            if node in visited:
                return visited[node]
            
            # Create deep copy of current node
            copy = Node(node.val)
            # Record copied node to visited
            visited[node] = copy
            # Iterate through current node's neighbors to copy them as well
            for nei in node.neighbors:
                copy.neighbors.append(dfs(nei))
            return copy

        return dfs(node) if node else None

        """
        Time complexity is O(V+E) because we need to visit each vertex and edge.
        Space complexity is O(V) because I used a hash map to store visited nodes.
        """