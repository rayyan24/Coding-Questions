class Solution:
    def minFlips(self, s: str) -> int:
        maxWindowSize=len(s) # size of the window 
        s=s+s
        newLen=len(s)
#       newLen is double the size of actual string
        alt1,alt2="",""
        diff1,diff2,left=0,0,0
        res=float("infinity")
        
        for i in range(newLen):
            alt1+="1" if i%2==0 else "0"
            alt2+="0" if i%2==0 else "1"
        
        for right in range(newLen):
            
            if s[right]!=alt1[right]:
                diff1+=1
            if s[right]!=alt2[right]:
                diff2+=1
#             increment left when window size gets larger than maxWindowSize
            
            if (right-left+1)>maxWindowSize:
                if s[left]!=alt1[left]:
                    diff1-=1
                if s[left]!=alt2[left]:
                    diff2-=1
                left+=1
            if (right-left+1)==maxWindowSize:
                res=min(res,diff1,diff2)
        return res