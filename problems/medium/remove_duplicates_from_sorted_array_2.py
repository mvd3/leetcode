class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        c = 1 # count
        r = 1

        for i in range(1, len(nums)):
            if nums[i] == nums[i-1]:
                c += 1
            else:
                c = 1
            if c <= 2:
                nums[r] = nums[i]
                r += 1

        return r