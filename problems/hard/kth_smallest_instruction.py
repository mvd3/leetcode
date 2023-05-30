import math

class Solution:
    def kthSmallestPath(self, destination: List[int], k: int) -> str:
        m, n = destination[1], destination[0] # number of moves
        mnp = math.factorial(m+n)/(math.factorial(m)*math.factorial(n))
        if mnp == k: # no need to compute last permutation
            return "".join(["V"] * n + ["H"] * m)
        s = k - 1 # permutation steps
        r = ["H"] * m + ["V"] * n # first permutation
        sp = m # "V" element position to be switched
        while s > 0:
            d = 0 # distance
            limit = 1
            while s > limit: # find upper limit
                d += 1
                limit = math.factorial(n+d)/(math.factorial(n)*math.factorial(d))
                if s <= limit:
                    break
            if s == limit: # in this case, only one character switching is needed
                r[sp], r[sp-d-1] = r[sp-d-1], r[sp]
                n -= 1
                break
            r[sp], r[sp-d] = r[sp-d], r[sp] # second case, when we have a remainder
            s -= math.factorial(n+d-1)/(math.factorial(n)*math.factorial(d-1))
            sp += 1
            n -= 1
        return "".join(r)