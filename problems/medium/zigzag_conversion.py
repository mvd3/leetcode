class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows == 1:
            return s
        
        n = len(s)
        d = 2 * (numRows - 1) # difference between positions
        r = ""

        for i in range(numRows):
            c = 0
            if i == 0 or i == numRows - 1:
                while c*d+i < n:
                    print(c*d+i)
                    r += s[c*d+i]
                    c += 1
            else:
                d1 = d - 2 * i
                while True:
                    if i+c*d < n:
                        r += s[i+c*d]
                        print(i+c*d)
                    if i+d1+c*d < n:
                        r += s[i+d1+c*d]
                        print(i+d1+c*d)
                        c += 1
                        continue
                    break

        return r