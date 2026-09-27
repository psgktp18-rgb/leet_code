class Solution(object):
    def findTargetSumWays(self, nums, target):
        dp = {}

        def solve(i, total):
            if i == len(nums):
                return total == target

            if (i, total) in dp:
                return dp[(i, total)]

            dp[(i, total)] = solve(i + 1, total + nums[i]) + solve(i + 1, total - nums[i])
            return dp[(i, total)]

        return solve(0, 0)