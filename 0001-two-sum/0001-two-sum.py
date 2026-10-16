class Solution(object):
    def twoSum(self, nums, target):
        d = {}

        for i in range(len(nums)):
            x = target - nums[i]

            if x in d:
                return ([d[x], i])
                break

            d[nums[i]] = i