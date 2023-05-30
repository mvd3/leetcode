class Solution:
    def candy(self, ratings: List[int]) -> int:
        n = len(ratings)
        c = [1] * n # candies to give

        for i in range(1, n): # left to right pass check
            c[i] = c[i-1]+1 if ratings[i] > ratings[i-1] else c[i]

        for i in range(n-2, -1, -1): # reverse pass to check again
            c[i] = c[i+1]+1 if ratings[i] > ratings[i+1] and c[i] <= c[i+1] else c[i]

        return sum(c)