class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        s=strs[0]
        for i in range(len(s)):
            for x in strs:
                if i==len(x) or x[i]!=s[i]:
                    return s[:i]
        return s