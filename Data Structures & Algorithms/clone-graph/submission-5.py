"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        visited = {}

        def dfs(node: Optional['Node']) -> Optional['Node']:
            if not node:
                return None
            if node in visited:
                return visited[node]
            
            cur = Node(node.val)
            visited[node] = cur

            for nei in node.neighbors:
                cur.neighbors.append(dfs(nei))

            return cur
        
        return dfs(node)