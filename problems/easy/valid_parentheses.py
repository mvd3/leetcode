class Solution:
    def isValid(self, s: str) -> bool:
        p = [] # stack

        for c in s:
            if c == "{" or c == "(" or c == "[":
                p.append(c)
                continue
            if len(p) == 0:
                return False
            if (c == "}" and p[-1] != "{") or (c == ")" and p[-1] != "(") or (c == "]" and p[-1] != "["):
                return False
            p.pop()

        return len(p) == 0