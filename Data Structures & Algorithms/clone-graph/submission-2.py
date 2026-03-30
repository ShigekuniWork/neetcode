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
        First, Iterate though while node is ramaining.
        Second, Append visited node to hash_mapto prevent from duplicted deep copy.
        """
        # Intialze response node and stack, visited node
        visited = {}

        # Declare dfs functions
        def dfs(node):
            # When current node in visited, return visited node
            if node in visited:
                return visited[node]
            
            # Crete deep copy of current node
            copy = Node(node.val)
            # Recode copied node to visited.
            visited[node] = copy
            # Iterate thought current node neighbors to copy as same.
            for nei in node.neighbors:
                copy.neighbors.append(dfs(nei))
            return copy

        return dfs(node) if node else None

        """
        Time complexity is O(V+E) because need to search each verteis and edges.
        Space complexity is O(V) because I used hash map for remaining visited node
        """
        