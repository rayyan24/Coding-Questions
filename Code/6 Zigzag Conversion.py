class Solution:
    def convert(self, s: str, nr: int) -> str:
        if nr==1: return s
        res=""
        inc=2*(nr-1)
        size=len(s)
        for curRow in range(nr):
            for j in range(curRow,size,inc):
#                 for the first and last rows
                res+=s[j]
#                 for middle rows
                k=j+inc-2*curRow
                if curRow>0 and curRow<nr-1 and k<len(s):
                    res+=s[j+inc-2*curRow]
        return res
class Solution:
    def convert(self, s: str, nr: int) -> str:
        if nr==1 or nr>=len(s): return s
        change=-1
        row=0
        res=[[] for i in range(nr)]
        for char in s:
            res[row].append(char)
            if row==0 or row==nr-1:
                change*=-1
            row+=change                
        
        for i in range(len(res)):
            res[i]="".join(res[i])
        return "".join(res)
            