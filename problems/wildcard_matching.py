import fnmatch

class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        return fnmatch.fnmatch(s, p)