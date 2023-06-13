class Solution:
    def intToRoman(self, num: int) -> str:
        s = [(1,"I"),(5,"V"),(10,"X"),(50,"L"),(100,"C"),(500,"D"),(1000,"M")] # symbols
        r = ""

        while num:
            s1 = s.pop() # first symbol
            x = num // s1[0]
            if x:
                r += s1[1] * int(x) # "M", "C", "X" and "I"
                num -= x * s1[0]
            if len(s) and 0.9*s1[0] <= num: # "CM", "XC", "IX"
                r += s[-2][1] + s1[1]
                num -= 0.9*s1[0]
            
            if num == 0:
                break
            
            s2 = s.pop() # second symbol
            x = num // s2[0]
            if x:
                r += s2[1]
                num -= s2[0]
            elif 0.8*s2[0] <= num:
                r += s[-1][1] + s2[1]
                num -= 0.8*s2[0]

        return r