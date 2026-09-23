class Solution:
    def selfDividingNumbers(self, left: int, right: int):
        ans = []

        for n in range(left, right + 1):
            temp = n
            ok = True

            while temp > 0:
                d = temp % 10

                if d == 0 or n % d != 0:
                    ok = False
                    break

                temp //= 10

            if ok:
                ans.append(n)

        return ans