# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        if len(lists) == 0:
            return None
        el = 0 # empty list
        for i in range(len(lists)):
            if lists[i] == None:
                el += 1
        if el == len(lists):
            return None

        
        h = ListNode() # head
        c = h # current
        m = [] # sorted list of minimum values

        for i in range(len(lists)):
            if lists[i]:
                m.append((lists[i].val, i)) # (value, position)
                lists[i] = lists[i].next # move to next
        
        m.sort(key=lambda x: x[0], reverse=True)

        while len(m):
            e = m.pop() # element
            c.val = e[0] # add to result list
            if lists[e[1]]: # check if not None
                m.append((lists[e[1]].val, e[1]))
                lists[e[1]] = lists[e[1]].next
                m.sort(key=lambda x: x[0], reverse=True)
            if len(m):
                c.next = ListNode()
                c = c.next

        return h