class Solution(object):
    def hasSameDigits(self, s):
        s = list(map(int, s))

        while len(s) > 2:
            new = []

            for i in range(len(s) - 1):
                new.append((s[i] + s[i + 1]) % 10)

            s = new

        return s[0] == s[1]