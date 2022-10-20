class Solution:
    def longestPalindrome(self, s: str) -> str:
        res = ""
        maxLen = 0
        size = len(s)
        # def helper(left,right):
        #     l=left
        #     r=right
        #     while l>=0 and r<=size and s[l]==s[r]:
        #         if r-l+1 >maxLen:
        #             res=s[l:r+1]
        #             maxLen=r-l+1
        #         l+=1
        #         r-=1

        for i in range(len(s)):
            #               odd len palindromes
            l = i
            r = i
            while l >= 0 and r < size and s[l] == s[r]:
                if r-l+1 > maxLen:
                    res = s[l:r+1]
                    maxLen = r-l+1
                l -= 1
                r += 1
#               even len palindromes
            l = i
            r = i+1
            while l >= 0 and r < size and s[l] == s[r]:
                if r-l+1 > maxLen:
                    res = s[l:r+1]
                    maxLen = r-l+1
                l -= 1
                r += 1
        return res
