class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        return re.match(fr"^{p}$", s) is not None