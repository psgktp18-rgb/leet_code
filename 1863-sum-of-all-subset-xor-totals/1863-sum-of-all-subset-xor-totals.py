class Solution(object):
    def subsetXORSum(self, nums):
        def dfs(i, xor):
            if i == len(nums):
                return xor

            take = dfs(i + 1, xor ^ nums[i])
            skip = dfs(i + 1, xor)

            return take + skip

        return dfs(0, 0)