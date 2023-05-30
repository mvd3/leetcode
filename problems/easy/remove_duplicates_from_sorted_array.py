class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        nl = sorted(set(nums)) # new list
        for i in range(len(nl)):
            nums[i] = nl[i]
        return len(nl)