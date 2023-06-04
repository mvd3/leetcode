class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices) # length
        r, m = 0, 0 # result, minimum position
        while m + 1 < n:
            if prices[m] > prices[m + 1]: # find local minimum
                m += 1
                continue
            break
        i = m + 1
        while i < n:
            while i + 1 < n:
                if prices[i + 1] >= prices[i]: # search for the local peak
                    i += 1
                    continue
                break
            r += prices[i] - prices[m] # add profit
            m = i + 1
            if m == n:
                break
            while m + 1 < n:
                if prices[m] > prices[m + 1]:
                    m += 1
                    continue
                break
            i = m + 1
        return r