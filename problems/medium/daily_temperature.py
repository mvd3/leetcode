class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        if len(temperatures) == 1:
            return [0]

        n = len(temperatures)
        r = [0] * n
        s = [] # stack

        for i in range(n):
            while len(s) and temperatures[s[-1]] < temperatures[i]:
                r[s[-1]] = i - s[-1]
                s.pop()
            s.append(i) 

        return r