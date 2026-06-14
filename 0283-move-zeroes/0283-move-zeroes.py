class Solution(object):
    def moveZeroes(self, nums):
        arr = []
        le = len(nums)

        for i in range(le):
            if nums[i] != 0:
                arr.append(nums[i])

        for i in range(le - len(arr)):
            arr.append(0)

        for i in range(le):
            nums[i] = arr[i]