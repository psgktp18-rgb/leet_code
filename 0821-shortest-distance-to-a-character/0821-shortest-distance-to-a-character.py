class Solution:
    def shortestToChar(self, s: str, c: str) -> List[int]:
        ans = []

        for i in range(len(s)):
            left = float('inf')
            right = float('inf')

            for j in range(i, -1, -1):
                if s[j] == c:
                    left = i - j
                    break

            for j in range(i, len(s)):
                if s[j] == c:
                    right = j - i
                    break

            ans.append(min(left, right))

        return ans