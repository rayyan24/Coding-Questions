class Solution:
    def makeGood(self, s: str) -> str:
# checks if current char and next char are upper and lower of each other
        def check(index):
            if abs(ord(s[index]) - ord(s[index+1])) == 32:
                return True
            return False
        i=0
        while i<=len(s)-2:
            if check(i): 
                s = s[:i] + s[i+2:]
                # for edge case if the ponter is always pointing at 0
                if i>0: i-=1 
            else:
                i+=1
        return s