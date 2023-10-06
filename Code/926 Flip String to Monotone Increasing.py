class Solution:
    def minFlipsMonoIncr(self, s: str) -> int:
        zeroFlip=0
        oneFlip=0
        ans=0
        for i in s:
            if i=="1":
                oneFlip+=1
            else:
                zeroFlip+=1
            zeroFlip=min(oneFlip,zeroFlip)
        return zeroFlip
