# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def getMinimumDifference(self, root: Optional[TreeNode]) -> int:
        v = [] # values

        def tli(node): # traverse list inorder
            if node:
                tli(node.left)
                v.append(node.val)
                tli(node.right)
        
        tli(root)
        
        r = v[1] - v[0]
        if r == 1:
            return r
        
        for i in range(2, len(v)):
            if v[i]-v[i-1] < r:
                r = v[i]-v[i-1]

        return r