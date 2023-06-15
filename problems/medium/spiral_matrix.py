class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        w, h = len(matrix[0]), len(matrix) # width, height
        r = [0] * (w*h)
        x, y, c = 0, 0, 0 # positions
        d = 0 # direction (0 - right, 1 - down, 2 - left, 3 - up)

        while c < len(r):
            if d == 0:
                for i in range(w):
                    r[c] = matrix[x][y]
                    y += 1
                    c += 1
                y -= 1 # prevent out of bounds
                h -= 1 # one row less
                x += 1 # move row down
                d = 1 # change direction
            elif d == 1:
                for i in range(h):
                    r[c] = matrix[x][y]
                    x += 1
                    c += 1
                x -= 1 # prevent out of bounds
                w -= 1
                y -= 1 # move column left
                d = 2
            elif d == 2:
                for i in range(w):
                    r[c] = matrix[x][y]
                    y -= 1
                    c += 1
                y += 1 # prevent out of bounds
                h -= 1
                x -= 1 # move row up
                d = 3
            else:
                for i in range(h):
                    r[c] = matrix[x][y]
                    x -= 1
                    c += 1
                x += 1 # prevent out of bounds
                w -= 1
                y += 1 # move column right
                d = 0
                
        return r