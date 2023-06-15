# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        if not list1 and not list2:
            return None
        if not list1 and list2:
            return list2
        if list1 and not list2:
            return list1
        
        h = list1 if list1.val <= list2.val else list2
        m = list2 if list1.val <= list2.val else list1

        c = h
        while m:
            while c.next:
                if c.next.val >= m.val:
                    break
                c = c.next
            t = m
            m = m.next
            t.next = c.next
            c.next = t

        return h