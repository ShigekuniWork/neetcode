# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        slow, fast = head, head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        second = slow.next
        slow.next = None

        prev = None
        while second:
            next_node = second.next
            second.next = prev
            prev = second
            second = next_node
        
        first, second = head, prev
        while second:
            next_node1, next_node2 = first.next, second.next
            first.next = second
            second.next = next_node1
            first, second = next_node1, next_node2





