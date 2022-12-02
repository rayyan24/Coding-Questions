class Solution:
    def halvesAreAlike(self, s: str) -> bool:
        def helper(Str):
            counter=0
            for char in Str:
                if char in {"a","e","i","o","u"}:
                    counter+=1
            return counter
            
        s=s.lower()
        a=s[:len(s)//2]
        b=s[len(s)//2:]
        A=helper(a)
        B=helper(b)
        return A==B
            
            
        
