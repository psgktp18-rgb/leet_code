class Solution:
    def reverse(self, x):
        if x < 0:
            x = str(x)
            r = "-" + x[1:][::-1]
            t = int(r)

            if t < -2147483648:
                return 0
            return t
        elif x==0:
            return 0
        else:
            x = str(x)
            r = x[::-1]
            r = r.lstrip("0")
            t = int(r)

            if t > 2147483647:
                return 0
            return t