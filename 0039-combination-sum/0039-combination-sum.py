class Solution:
    def combinationSum(self, candidates, target):

        ans = []

        def solve(i, path, total):

            if total == target:
                ans.append(path[:])
                return

            if total > target or i == len(candidates):
                return

            # Choose current number
            path.append(candidates[i])
            solve(i, path, total + candidates[i])
            path.pop()

            # Skip current number
            solve(i + 1, path, total)

        solve(0, [], 0)

        return ans