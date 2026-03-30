# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        """
        I'd appach this problem by using BFS.
        First, I store root to the deque.
        Second, Iterate thought deque and sotre the value of the current node to result each level
        """
        if root is None:
            return []

        # Set up deque to store iterate each of lovels
        # initial value is current root
        queue = deque()
        queue.append(root)
        # Assing empty list to 'result'
        result = []

        # Iterate thought while existing queue
        while queue:
            # Assing empty list to cur_levels
            cur_levels = []
            queue_lenght = len(queue)
            # Iterate though queue to get value of current levles
            for _ in range(queue_lenght):
                # Append value poped from the queue
                cur = queue.popleft()
                cur_levels.append(cur.val)
                # if left node, right node of current node, append to queue
                if cur.left:
                    queue.append(cur.left)
                if cur.right:
                    queue.append(cur.right)
            # then append the result of current levels to result
            result.append(cur_levels)
        
        return result
        """
        The time complexity is O(n) because every node in the tree is visited once.
        The space complexity is O(n) as well because, in the worst case, 
        the queue can hold all nodes at the widest level of the tree.
        """
