class Solution:
    def reverseWords(self, s: str) -> str:
        t=s.split()[::-1]
        res=""
        for i in t:
            res=res+" " +i
        return res.strip()