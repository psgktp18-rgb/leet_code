class Solution:
    def minimumRecolors(self, blocks: str, k: int) -> int:
        l=0
        re=0
        res=k
        for r in range(len(blocks)):
            if blocks[r]=="W":
                re+=1
            if r-l+1==k:
                res=min(re,res)
                if blocks[l]=="W":    
                    re-=1
                l+=1
        return res