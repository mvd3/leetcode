class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        if sum(gas) < sum(cost): # There is no solution
            return -1
        
        n = len(gas)
        c, p = 0, 0 # current fuel, starting position
        for i in range(n):
            c += gas[i] - cost[i]
            if c < 0:
                p = i + 1
                c = 0
        
        return p