class Solution(object):
    def longestNiceSubstring(self, s):
        if len(s) < 2:
            return ""

        st = set(s)

        for i in range(len(s)):
            if s[i].swapcase() not in st:
                left = self.longestNiceSubstring(s[:i])
                right = self.longestNiceSubstring(s[i+1:])

                if len(left) >= len(right):
                    return left
                else:
                    return right

        return s