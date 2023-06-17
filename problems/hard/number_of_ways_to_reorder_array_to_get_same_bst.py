class Solution:
    def numOfWays(self, nums: List[int]) -> int:
        m = 10 ** 9 + 7 # modulo factor

        def stvp(t): # subtree valid permutations
            if len(t) < 3:
                return 1
            lst = [x for x in t if x < t[0]] # left subtree
            rst = [x for x in t if x > t[0]] # right subtree
            return (stvp(lst) * stvp(rst) * comb(len(t) - 1, len(lst))) % m # result
        
        return (stvp(nums) - 1) % m