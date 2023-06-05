class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        n = len(isConnected)
        r = 0
        v = [False] * n # visited

        def dfs(i): # deep field search
            v[i] = True
            for j in range(n):
                if isConnected[i][j] and not v[j]: # seek unvisited neighbours
                    dfs(j)

        for i in range(n):
            if not v[i]:
                r += 1
                dfs(i)

        return r