class Solution:
    def maxArea(self, height: List[int]) -> int:
        n = len(height)
        r = 0
        lsp, rsp = [0], [n-1] # left/right side positions
        
        for i in range(1, n):
            if height[i] > height[lsp[-1]]: # seek greater height
                lsp.append(i)
        
        for i in range(n-1, -1, -1):
            if height[i] > height[rsp[-1]]:
                rsp.append(i)

        i, j = 0, 0
        while lsp[i] < rsp[j]:
            a = (rsp[j]-lsp[i])*min(height[rsp[j]], height[lsp[i]]) # area
            
            if a > r:
                r = a
            if height[lsp[i]] > height[rsp[j]] and j + 1 < len(rsp):
                j += 1
            elif i + 1 < len(lsp):
                i += 1
            else:
                break

        return r