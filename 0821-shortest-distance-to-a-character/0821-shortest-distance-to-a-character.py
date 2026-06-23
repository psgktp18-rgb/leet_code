class Solution:
    def shortestToChar(self, s: str, c: str) -> List[int]:
        p = [i for i, ch in enumerate(s) if ch == c]
        return [min(abs(i - j) for j in p) for i in range(len(s))]