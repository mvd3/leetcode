from sortedcontainers import SortedSet

class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return 0
        ns = set(nums) # nums set
        m = 1 # if all elements are unique
        for i in range(len(nums)):
            c = 1
            if nums[i]-1 not in ns: # seek the lowest number in sequence
                while nums[i]+c in ns: # seek the length
                    c += 1
                m = c if c > m else m # check if it is the largest sequence
        return m