class Solution:
    def helper(self,S,left,right):
        res=0
        while left>=0 and right<len(S) and S[left]==S[right]:
            res+=1
            left-=1
            right+=1
        return res
    def countSubstrings(self, s: str) -> int:
        res=0
        size=len(s)
        '''
start from 0 index upto len(s)-1 expand towards left and right if s[l]==s[r] it is a palindrome 
        '''
        for i in range(size):
#             for odd len substrings
            res+=self.helper(s,i,i)
#             for even len substrings
            res+=self.helper(s,i,i+1)
        return res
        