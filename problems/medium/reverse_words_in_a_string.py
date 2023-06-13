class Solution:
    def reverseWords(self, s: str) -> str:
        r = list(filter(lambda x: len(x), s.split(" ")))
        r.reverse()
        return " ".join(r)