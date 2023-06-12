class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        if len(t) == 0 and len(s) > 0:
            return False
        if len(s) == 0:
            return True
        
        i = 0 # index for s
        for c in t:
            if c == s[i]:
                i += 1
                if i == len(s):
                    return True
        return False