class Solution:
    def reverseBits(self, n: int) -> int:
        b = bin(n)[2::]
        b=b.zfill(32)
        b=b[::-1]
        b=int(b,2)
        return (b)