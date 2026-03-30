# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        self.ancestor = root

        if p.val > q.val:
            p , q = q , p


        def dfs(root: Optional[TreeNode]):
            if not root:
                return
            
            if p.val < root.val and root.val < q.val:
                self.ancestor = root
                return
            
            if p.val == root.val or q.val == root.val:
                self.ancestor = root
                return
            
            if q.val < root.val:
                dfs(root.left)
            else:
                dfs(root.right)

        dfs(root)
        return self.ancestor