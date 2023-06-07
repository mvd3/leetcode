class Solution:
    def minFlips(self, a: int, b: int, c: int) -> int:
        r = 0
        while a or b or c:
            bitA, bitB, bitC = a & 1, b & 1, c & 1

            if bitC == 0: # switching any 1 to 0
                r += bitA + bitB
            elif bitA == 0 and bitB == 0: # bitC is 0, so one bit needs to be switched to 1
                r += 1
            
            a >>= 1
            b >>= 1
            c >>= 1
        return r            