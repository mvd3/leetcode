class Solution:
    def trap(self, height: List[int]) -> int:
        n = len(height)
        r = 0
        rp = [] # region border position
        
        if sum(height) == max(height): # check if there is something to keep the water
            return r

        for i in range(n): # seek first border
            if height[i]:
                rp.append(i)
                break
        for i in range(rp[-1]+1, n): # seeking border with max height
            if height[i] >= height[rp[-1]]:
                rp.append(i)
        
        mp = rp[-1] # max height position
        mpi = len(rp) - 1 # index of mp in rp
        for i in range(n-1, mp, -1): # right side border
            if height[i]:
                rp.append(i)
                break
        if rp[-1] != mp: # in case there is one
            for i in range(rp[-1]-1, mp, -1):
                if height[i] >= height[rp[mpi+1]]:
                    rp.insert(mpi+1, i)
        
        for i in range(mpi):
            wl = height[rp[i]] # water level
            for j in range(rp[i]+1, rp[i+1]):
                r += wl - height[j]

        for i in range(len(rp)-1, mpi, -1):
            wl = height[rp[i]]
            for j in range(rp[i]-1, rp[i-1], -1):
                r += wl - height[j]

        return r