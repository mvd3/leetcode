class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(s) == 0:
            return 0
        if len(s) == 1:
            return 1

        r = 0
        sp = 0 # starting position
        d = { s[sp]: 0 } # dictionary

        for i in range(1, len(s)):
            if s[i] not in d:
                d[s[i]] = i # add position of character into dictionary
                continue
            r = max(r, len(d))
            while s[sp] != s[i]:
                del d[s[sp]]
                sp += 1
            d[s[sp]] = i
            sp += 1

        r = max(r, len(d))

        return r