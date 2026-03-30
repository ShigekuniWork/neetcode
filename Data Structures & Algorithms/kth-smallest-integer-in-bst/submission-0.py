# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        self.k = k
        def dfs(root: Optional[TreeNode], arr: set):
            if len(arr) >= self.k:
                return arr
            
            if root is None:
                return None

            left = dfs(root.left, arr)
            right = dfs(root.right, arr)
            
            arr.add(root.val)
            
            if left:
                arr = left | arr
            if right:
                arr = arr | right

            return arr

        arr = dfs(root, set())
        return list(arr)[k-1]