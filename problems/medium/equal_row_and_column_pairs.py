class Solution:
    def equalPairs(self, grid: List[List[int]]) -> int:
        n = len(grid)
        r = 0
        
        for i in range(n):
            c = 0
            for j in range(n):
                while grid[i][c] == grid[c][j]:
                    c += 1
                    if c == n:
                        r += 1
                        break
                c = 0

        return r