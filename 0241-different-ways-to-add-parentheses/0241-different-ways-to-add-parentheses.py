class Solution:
    def isNum(self, c):
        return c >= '0' and c <= '9'

    def solve(self, i, j, exp):

        if i == j:
            return [int(exp[i])]

        if j - i <= 1 and self.isNum(exp[i]) and self.isNum(exp[j]):
            return [int(exp[i]) * 10 + int(exp[j])]

        if (i, j) in self.dp:
            return self.dp[(i, j)]

        posAns = []

        for k in range(i + 1, j):

            if self.isNum(exp[k]):
                continue

            leftSolution = self.solve(i, k - 1, exp)
            rightSolution = self.solve(k + 1, j, exp)

            for x in leftSolution:
                for y in rightSolution:

                    if exp[k] == '*':
                        posAns.append(x * y)

                    elif exp[k] == '-':
                        posAns.append(x - y)

                    elif exp[k] == '+':
                        posAns.append(x + y)

        self.dp[(i, j)] = posAns
        return posAns

    def diffWaysToCompute(self, expression):
        self.dp = {}
        return self.solve(0, len(expression) - 1, expression)