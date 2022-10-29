class Solution:
    def titleToNumber(self, ct: str) -> int:
        res=0
        for char in ct:
            # res=res*26+(ord(char)-65+1)
            res=res*26+(ord(char)-64)
        return res