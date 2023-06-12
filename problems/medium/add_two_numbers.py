class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        a, b = "", ""
        n = l1
        while n:
            a = str(n.val) + a
            n = n.next
        n = l2
        while n:
            b = str(n.val) + b
            n = n.next
        s = [int(x) for x in [*str(int(a)+int(b))]] # sum
        r = ListNode() # head/result
        c = r # current
        for i in range(len(s)-1, -1, -1):
            c.val = s[i]
            if i > 0:
                c.next = ListNode()
                c = c.next
        return r