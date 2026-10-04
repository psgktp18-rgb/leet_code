class Solution(object):
    def subsetXORSum(self, nums):
        x = 0

        for num in nums:
            x |= num

        return x * (2 ** (len(nums) - 1))