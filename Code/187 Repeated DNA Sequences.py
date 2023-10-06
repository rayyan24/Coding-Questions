class Solution:
    def findRepeatedDnaSequences(self, s: str) -> List[str]:
        temp=set()
        res=set()
        left=0
        size=len(s)
#       size-9 so that our window never gets out of bound and always have 10 characters
        while left<size-9:
            right=left+10
            cur=s[left:right]
            if cur in temp:
                res.add(cur)
            else:
                temp.add(cur)
            left+=1
        return list(res)