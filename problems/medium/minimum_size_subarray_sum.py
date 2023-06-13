class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        if sum(nums) < target:
            return 0
        if max(nums) >= target:
            return 1
        
        n = len(nums)
        l, r, t, w = 0, 0, 0, n+1 # left, right, total, width

        while r < n:
            t += nums[r]
            r += 1
            while t >= target:
                w = min(w, r-l)
                t -= nums[l]
                l += 1
        
        return w