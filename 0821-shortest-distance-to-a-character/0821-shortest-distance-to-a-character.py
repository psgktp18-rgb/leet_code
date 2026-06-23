class Solution:
    def shortestToChar(self, s: str, c: str) -> List[int]:
        ans=[]
        for i in range(len(s)):
            mn = len(s)

            for j in range(len(s)):
                if s[j] == c:
                    mn = min(mn, abs(i - j))

            ans.append(mn)

        return ans