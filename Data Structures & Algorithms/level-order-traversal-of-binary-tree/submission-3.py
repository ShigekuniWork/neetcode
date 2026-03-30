# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        response = []

        def dfs(root: Optional[TreeNode], depth: int):
            if root is None:
                return None
            
            if len(response) == depth:
                response.append([])
            
            response[depth].append(root.val)
            dfs(root.left, depth+1)
            dfs(root.right, depth+1)
        
        dfs(root, 0)

        return response
