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

        def dfs(root):
            if not root:
                return None
            
            if root.val in visited:
                return visited[root.val]
            
            copy_node = Node(root.val)
            visited[root.val] = copy_node

            for adj in root.neighbors:
                copy_node.neighbors.append(dfs(adj))
            return copy_node

        return dfs(node)