class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        n = 0
        for i in range(len(nums)):
            if nums[i] == val:
                nums[i] = 51
                n += 1
        nums.sort()
        return len(nums)-n