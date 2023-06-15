# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxLevelSum(self, root: Optional[TreeNode]) -> int:
        if not root.left and not root.right:
            return 1
        
        r = 1
        m = root.val # maximal value
        q = [root] # level queue
        qs = 1 # queue (level) size
        c = 0

        while q:
            c += 1 # current level
            s = 0 # level sum
            for i in range(qs):
                s += q[0].val
                if q[0].left:
                    q.append(q[0].left)
                if q[0].right:
                    q.append(q[0].right)
                q.pop(0) # pop first element
            if s > m:
                r = c
                m = s
            qs = len(q)

        return r