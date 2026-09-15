class Solution(object):
    def hammingWeight(self, n):
        """
        :type n: int
        :rtype: int
        """
        b=(bin(n)[2:])
        c=b.count("1")
        return c