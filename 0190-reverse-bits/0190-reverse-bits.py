class Solution:
    def reverseBits(self, n: int) -> int:
        b = bin(n)[2:]
        b=b.zfill(32)
        v=b[::-1]
        v=int(v,2)
        return (v)