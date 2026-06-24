class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        """
        nums.sort()
        for i in range(len(nums)):
            for j in range(i+1,len(nums)):
                for k in range(j+1,len(nums)):
                    if nums[i]+nums[j]+nums[k]==0:
                        return nums[i],nums[j],nums[k]
                        continue
                    else:
                    ans = []
            """
        """
        nums.sort()
        ans=[]
        for i in range(len(nums)):
            for j in range(i+1, len(nums)):
                for k in range(j+1, len(nums)):
                    if nums[i] + nums[j] + nums[k] == 0:
                        t = [nums[i], nums[j], nums[k]]
                        if t not in ans:
                            ans.append(t)

        return ans
        """
        nums.sort()
        ans = []

        for i in range(len(nums)):

            if i > 0 and nums[i] == nums[i-1]:
                continue

            left = i + 1
            right = len(nums) - 1

            while left < right:
                s = nums[i] + nums[left] + nums[right]

                if s == 0:
                    ans.append([nums[i], nums[left], nums[right]])

                    left += 1
                    right -= 1

                    while left < right and nums[left] == nums[left-1]:
                        left += 1

                    while left < right and nums[right] == nums[right+1]:
                        right -= 1

                elif s < 0:
                    left += 1
                else:
                    right -= 1

        return ans