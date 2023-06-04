class Solution:
    def canJump(self, nums: List[int]) -> bool:
        n = len(nums) # size
        if nums[0] == 0 and n > 1:
            return False
        elif n == 1:
            return True
        c = nums[0]
        for i in range(1, n-1):
            c = nums[i] if nums[i] > c - 1 else c - 1
            if c == 0:
                return False
        return True