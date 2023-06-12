class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        if len(nums) == 0:
            return []
        if len(nums) == 1:
            return [str(nums[0])]
        
        r = []
        s = 1 # range size
        i = 0 # index
        while i + s < len(nums):
            if nums[i] + s == nums[i+s]:
                s += 1
                continue
            r.append(str(nums[i]))
            if s > 1:
                r[-1] += "->" + str(nums[i+s-1])
            i += s
            s = 1
        r.append(str(nums[i]))
        if s > 1:
                r[-1] += "->" + str(nums[i+s-1])

        return r