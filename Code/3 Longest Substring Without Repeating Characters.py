class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        Set=set()
        left=0
        res=0
#         using sliding window technique
        for right in range(len(s)):
            CE=s[right]
            while CE in Set:
                Set.remove(s[left])
                left+=1
            # only add in set when any copy of CE is not in set and calculate max 
            Set.add(CE)
            res=max(res,right-left+1)
        return res
            


def areDistinct(str, i, j):
    # Note : Default values in visited are false
    visited = [0] * (26)
    for k in range(i, j + 1):
        # 97 is ascii val of "a"
        # if visited[0]=1 means "a" has already been occored in string
        # if visited[1]=1 means "b" has already been occored in string and so on
        curChar = ord(str[k]) - 97
        if visited[curChar] == True:
            return False
        visited[curChar] = True
    return True


def longestUniqueSubsttr(str):

    n = len(str)
    # for a string of length n (n*(n+1))/2 substrings are possible
    res = 0
    for i in range(n):
        for j in range(i, n):
            if (areDistinct(str, i, j)):
                res = max(res, j - i + 1)
            # print(str[i:j+1])
    print(res)


longestUniqueSubsttr("abcfdsff")
# print(ord("k")-ord(a))
