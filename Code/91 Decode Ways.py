class Solution:
    def numDecodings(self, s: str) -> int:
        # chr converts ascii value to its corresponding char
        size=len(s)
        def isValid(index):
            if (index + 1 < size and (s[index] == '1' or (s[index] == '2' and s[index+1] in"0123456"))):
                return True
            return False
        
        
        
        dp={size:1} #print(dp) --->{2: 1} for s="12"
        for index in range(size-1,-1,-1):
            if s[index]=="0":
                dp[index]=0
#           taking only the current digit one digit
            else: 
                dp[index]=dp[index+1]
#             checking if two digiits 
            if isValid(index):
                dp[index]=dp[index]+dp[index+2]
        return dp[0]
