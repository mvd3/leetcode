class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        if len(nums1) == 0 or len(nums2) == 0:
            return nums1 if len(nums1) == 0 else nums2
        for i in range(n):
            nums1[m + i] = nums2[i]
        nums1.sort()