from math import gcd

class Solution:
    def maxPairStrength(self, nums):
        ans = 0

        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):
                g = gcd(nums[i], nums[j])
                strength = (nums[i] // g) * (nums[j] // g)
                ans = max(ans, strength)

        return ans