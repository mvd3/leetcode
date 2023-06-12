class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        r = 0
        s = [] # stack
        for i, v in enumerate(heights):
            p = i # start position
            while s and s[-1][1]>v:
                e = s.pop()
                r = max(r,(i-e[0])*e[1])
                p = e[0]
            s.append((p,v))
        for i,h in s:
            r=max(r,h*(len(heights)-i))
        return r