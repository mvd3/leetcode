class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        result = set()
        nums.sort()

        for i in range(len(nums)-2):
            l = i + 1 # left position
            r = len(nums) - 1 # right position
            while l < r:
                s = nums[i] + nums[l] + nums[r] # sum
                if s == 0: # match, add to set and move
                    result.add((nums[i], nums[l], nums[r]))
                    l += 1
                    r -= 1
                elif s > 0: # move down
                    r -= 1
                else: # move up
                    l += 1

        return result