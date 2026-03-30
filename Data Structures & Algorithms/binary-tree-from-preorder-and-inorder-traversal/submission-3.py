# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        self.preIndex = 0
        self.InIndex = 0

        def dfs(limit):
            if self.preIndex >= len(preorder):
                return None
            if inorder[self.InIndex] == limit:
                self.InIndex += 1
                return None
            
            node = TreeNode(preorder[self.preIndex])
            self.preIndex += 1
            node.left = dfs(node.val)
            node.right = dfs(limit)

            return node

        return dfs(float('INF'))
