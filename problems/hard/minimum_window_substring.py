class Solution:
    def minWindow(self, s: str, t: str) -> str:
        n = len(s)
        cc = Counter(t) # character counter from pattern
        cs = len(cc) # counter size
        sp, i = 0, 0 # start position, index
        r = n + 1 # result (default)

        for j in range(n):
            if s[j] in cc: # found character from pattern
                cc[s[j]] -= 1
                if cc[s[j]] == 0:
                    cs -= 1 # one character less from pattern
            while cs == 0: # found substring
                if r > j - i + 1: # check if substring is shorter
                    r = j - i + 1 # set to shorter
                    sp = i # new start position
                if s[i] in cc:
                    cc[s[i]] += 1 # return to counter
                    if cc[s[i]] > 0: # increase counter size
                        cs += 1
                i += 1

        if r > n:
            return ""
        return s[sp:sp+r]