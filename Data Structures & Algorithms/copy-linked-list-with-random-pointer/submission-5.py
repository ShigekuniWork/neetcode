"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        if head is None:
            return None
        
        cur = head
        while cur:
            copy_node = Node(cur.val)
            copy_node.next = cur.next
            cur.next = copy_node
            cur = copy_node.next
        
        response = head.next

        cur = head
        while cur:
            if cur.random:
                cur.next.random = cur.random.next
            cur = cur.next.next
        
        cur = head
        while cur:
            copy_node = cur.next
            cur.next = copy_node.next
            if copy_node.next:
                copy_node.next = copy_node.next.next
            cur = cur.next

        return response