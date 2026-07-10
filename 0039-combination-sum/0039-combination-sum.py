class Solution(object):
    def combinationSum(self, candidates, target):
        ans = []
        path = []

        def dfs(target, start):
            if target == 0:
                ans.append(path[:])
                return

            if target < 0:
                return

            for i in range(start, len(candidates)):
                path.append(candidates[i])
                dfs(target - candidates[i], i)
                path.pop()

        dfs(target, 0)
        return ans