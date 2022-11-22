class Solution:
    def guessNumber(self, n: int) -> int:
        l=1
        r=n
        res=0
        while l<=r:
            mid=(l+r)//2
            curr=guess(mid)
            if curr==-1:
                r=mid-1
            elif curr==1:
                l=mid+1
            elif curr==0:
                res=mid
                break
        return res