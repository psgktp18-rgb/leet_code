class Solution:
    def partition(self, s: str) -> list[list[str]]:
        res = []
        path = []

        def backtrack(start):
            if start == len(s):
                res.append(path[:])
                return

            for end in range(start, len(s)):
                sub = s[start:end+1]

                if sub == sub[::-1]:
                    path.append(sub)
                    backtrack(end + 1)
                    path.pop()

        backtrack(0)
        return res