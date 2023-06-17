class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        if len(matrix) == 1:
            return
        n = len(matrix)
        lc = n // 2 # layer count
        for i in range(lc):
            w = n - 2 * i - 1 # layer width
            p = [i, i, i, i + w, i + w, i + w, i + w, i] # positions
            for j in range(w):
                matrix[p[0]][p[1]], matrix[p[2]][p[3]], matrix[p[4]][p[5]], matrix[p[6]][p[7]] = matrix[p[6]][p[7]], matrix[p[0]][p[1]], matrix[p[2]][p[3]], matrix[p[4]][p[5]]
                p[1] += 1
                p[2] += 1
                p[5] -= 1
                p[6] -= 1