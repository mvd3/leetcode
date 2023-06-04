class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        r = [] # all elememnts will be stored here
        for i in range(9):
            for j in range(9):
                e = board[i][j]
                if e != ".":
                    r += [(i, e), (e, j), (i // 3, j // 3, e)] # print set(r) to understand this solution
        return len(r) == len(set(r))