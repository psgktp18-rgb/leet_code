
class Solution:
    def smallestUniqueSubarray(self, nums: List[int]) -> int:
        n = len(nums)

        def check(length):
            base1, base2 = 100019, 100043
            mod1, mod2 = 10**9 + 7, 10**9 + 9

            power1 = pow(base1, length, mod1)
            power2 = pow(base2, length, mod2)

            h1 = h2 = 0
            freq = {}

            # First window
            for i in range(length):
                h1 = (h1 * base1 + nums[i]) % mod1
                h2 = (h2 * base2 + nums[i]) % mod2

            freq[(h1, h2)] = 1

            # Remaining windows
            for i in range(length, n):
                h1 = (h1 * base1 - nums[i-length] * power1 + nums[i]) % mod1
                h2 = (h2 * base2 - nums[i-length] * power2 + nums[i]) % mod2

                key = (h1, h2)
                freq[key] = freq.get(key, 0) + 1

            return 1 in freq.values()

        # Binary Search
        left, right = 1, n

        while left < right:
            mid = (left + right) // 2

            if check(mid):
                right = mid
            else:
                left = mid + 1

        return left
