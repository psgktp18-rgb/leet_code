class Solution:
    def uniquePathsIII(self, grid):

        m = len(grid)
        n = len(grid[0])

        ans = 0
        need = 0

        sol = [[0] * n for _ in range(m)]

        for i in range(m):
            for j in range(n):
                if grid[i][j] != -1:
                    need += 1

                if grid[i][j] == 1:
                    sr, sc = i, j

        def dfs(r, c, visited):
            nonlocal ans

            if r < 0 or c < 0 or r >= m or c >= n:
                return

            if grid[r][c] == -1:
                return

            if sol[r][c] == 1:
                return

            if grid[r][c] == 2:
                if visited == need:
                    ans += 1
                return

            sol[r][c] = 1

            dfs(r + 1, c, visited + 1)
            dfs(r - 1, c, visited + 1)
            dfs(r, c + 1, visited + 1)
            dfs(r, c - 1, visited + 1)

            sol[r][c] = 0

        dfs(sr, sc, 1)

        return ans