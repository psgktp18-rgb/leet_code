class Solution:
    def reverseBits(self, n: int) -> int:
        b = bin(n)[2::]
        z=b.zfill(32)
        v=z[::-1]
        v=int(v,2)
        return (v)