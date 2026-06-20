class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        d = {}

        for x in nums:
            d[x] = d.get(x, 0) + 1

        for x in d:
            if d[x] > len(nums)//2:
                return x