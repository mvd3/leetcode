class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        n = len(nums)
        k %= n
        if k > 0:
            t = nums[-k:] # Right part of shift
            nums[k:] = nums[:-k] # Left part moving to right
            nums[:k] = t # Placing the right part