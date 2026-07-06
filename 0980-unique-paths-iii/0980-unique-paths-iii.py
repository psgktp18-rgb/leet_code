class Solution:
    def uniquePathsIII(self, g):
        row = len(g)
        cols = len(g[0])
        e = 0
        for i in range(row):
            for j in range(cols):
                if g[i][j] != -1:
                    e += 1
                if g[i][j] == 1:
                    sr = i
                    sc = j
        def vasanth(r,c,rem):
            if r<0 or r>=row or c<0 or c>=cols:
                return False
            if g[r][c] == -1:
                return False
            if g[r][c] == 2:
                if rem == 1:   
                    return True
                return False

            temp = g[r][c]
            g[r][c] = -1
            p = 0
            p += vasanth(r+1,c,rem-1)
            p += vasanth(r-1,c,rem-1)
            p += vasanth(r,c+1,rem-1)
            p += vasanth(r,c-1,rem-1)
            g[r][c] = temp
            return p
        return vasanth(sr,sc,e)