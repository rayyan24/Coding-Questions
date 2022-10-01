class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        Map={
            "2":"abc",
            "3":"def",
            "4":"ghi",
            "5":"jkl",
            "6":"mno",
            "7":"pqrs",
            "8":"tuv",
            "9":"wxyz"  
        }
        res=[]
        lenDigits=len(digits)
        def helper(pos,curStr):
            if len(curStr)==lenDigits:
                res.append(curStr)
                return
            # call same function for all the chars mapped with digits at current position 
            for char in Map[digits[pos]]:
                helper(pos+1,curStr+char)
        if lenDigits is not 0:
            helper(0,"")
        return res
            
            