class Solution:
    def fullJustify(self, words: List[str], maxWidth: int) -> List[str]:
        r = [] # result
        words.reverse() # reversing the list for easier operations
        while len(words):
            s = [] # string
            ss = 0 # string size (without whitespaces)
            while len(words[-1]) + ss + len(s) <= maxWidth: # check if next word fits
                ss += len(words[-1])
                s.append(words.pop())
                if len(words) == 0:
                    break
            if len(words): # not the last line
                # whitespaces between words
                ws = (maxWidth - ss) // (len(s) - 1) if len(s) > 1 else maxWidth - ss
                # remaining white spaces (for left side)
                rws = (maxWidth - ss) % (len(s) - 1) if len(s) > 1 else 0
                # result string
                if len(s) > 1:
                    if rws:
                        rs = ((ws+1)*" ").join(s[:rws]) + (ws+1) * " " + (ws * " ").join(s[rws:])
                    else:
                        rs = (ws * " ").join(s[rws:])
                else:
                    rs = s[0] + (ws * " ")
                r.append(rs)
            else: # last line
                r.append(" ".join(s) + (maxWidth - ss - len(s) + 1) * " ")
        return r