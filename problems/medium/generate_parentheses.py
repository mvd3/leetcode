class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        rs = []

        def build(l, r, s): # left, right, string
            if len(s) == 2 * n:
                rs.append(s)
                return
            if l < n:
                build(l+1, r, s + '(')
            if r < l:
                build(l, r+1, s + ')')

        build(0, 0, '')
        return rs