class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        r, m = 0, prices[0] # result, minimal
        for i in range(1, len(prices)):
            if prices[i] < m:
                m = prices[i]
            elif prices[i] > m:
                r = max(prices[i]-m, r)
        return r