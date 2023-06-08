class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        c = [100001, 100001] # cost
        p = [0, 0] # profit

        for s in prices: # stock
            c[0] = min(c[0], s)
            p[0] = max(p[0], s - c[0])
            c[1] = min(c[1], s - p[0])
            p[1] = max(p[1], s - c[1])
        
        return p[1]