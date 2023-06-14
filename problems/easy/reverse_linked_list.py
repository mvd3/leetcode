# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return None
        if not head.next:
            return head
        
        c, n = head, head.next # current, next
        c.next = None

        while n:
            t = n.next # temporary
            n.next = c
            c = n
            n = t
        
        return c