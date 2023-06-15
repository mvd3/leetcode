# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if k == 1:
            return head

        n = 0
        c = head
        while c:
            n += 1
            c = c.next

        g = n // k # number of groups        
        f = p = head # first, previous
        c = head.next

        for i in range(1, k):
            t = c.next
            c.next = p
            p = c
            c = t

        f.next = c # connect lists
        if g == 1: # no more groups
            return p

        nh = p # new head
        for i in range(1, g):
            pg = f # previous group
            f = p = c
            c = c.next
            for j in range(1, k):
                t = c.next
                c.next = p
                p = c
                c = t
            pg.next = p
            f.next = c

        return nh