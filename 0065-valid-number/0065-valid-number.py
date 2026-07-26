class Solution:
    def isNumber(self, s: str) -> bool:
        digit = False
        dot = False
        exp = False
        digit_after_exp = True

        for i in range(len(s)):
            c = s[i]

            if c.isnumeric():
                digit = True
                if exp:
                    digit_after_exp = True

            elif c == '+' or c == '-':
                if i > 0 and s[i - 1] not in 'eE':
                    return False

            elif c == '.':
                if dot or exp:
                    return False
                dot = True

            elif c == 'e' or c == 'E':
                if exp or not digit:
                    return False

                exp = True
                digit_after_exp = False

            else:
                return False

        return digit and digit_after_exp