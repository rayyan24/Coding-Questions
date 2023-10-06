# 1898 Maximum Number of Removable Characters
class Solution:
    def maximumRemovals(self, s: str, p: str, arr: List[int]) -> int:
        def helper(mainStr,subseq):
            i,j=0,0
            while i<lenS and j<lenP:
                if i in removed or mainStr[i]!=subseq[j]:
                    i+=1
                else:
                    i+=1
                    j+=1
            return j==lenP
        left,right=0,len(arr)-1
        ans=0
        lenS,lenP=len(s),len(p)
        while left<=right:
            mid=(left+right)//2
            removed=set(arr[:mid+1])
            if helper(s,p):
                ans=max(ans,mid+1)
                left=mid+1
            else:
                right=mid-1
        return ans
                