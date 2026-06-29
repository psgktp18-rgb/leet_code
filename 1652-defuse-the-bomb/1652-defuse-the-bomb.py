class Solution:
    def decrypt(self, code: List[int], k: int) -> List[int]:
        n=len(code)
        res=[0]*len(code)
        for i in range(len(code)):
            if k>0:
                for j in range(i+1,i+1+k):
                    res[i]+=code[j%n]
            if k<0:
                for j in range(i-1,i-1-abs(k),-1):
                    res[i]+=code[j%n]
        return res
