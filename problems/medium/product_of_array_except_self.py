class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        zc = [] # zero count
        for i in range(n):
            if nums[i] == 0:
                zc.append(i)
        if len(zc) > 1: # all null
            return [0] * n
        elif len(zc) == 1: # only one non-zero number 
            p = 1
            for i in range(zc[0]):
                p *= nums[i]
            for i in range(zc[0]+1, n):
                p *= nums[i]
            return [0] * zc[0] + [p] + [0] * (n - zc[0] - 1)
        
        r = [1] * n

        for i in range(1, n): # left pass
            r[i] = r[i-1] * nums[i-1]
        
        rp = 1 # right side product
        for i in range(n-1, -1, -1):
            r[i] *= rp
            rp *= nums[i]
        return r