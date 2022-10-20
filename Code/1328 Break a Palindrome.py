class Solution:
    def breakPalindrome(self, s: str) -> str:
#         We need to replace one symbol and to get the smallest string as possible. First, we try to change elements on the smaller positions: imagine we have string xyzyx - where x, y, z can be any symbols. If x is not equal to "a", then if we replace this symbol with "a" we will break palindrome and it will be as small as possible. However if x = "a", it is not optimal to replace it to say "b", we can only make our string bigger. So, we move to the next element y and so on. Notice that we can not change z in this case, because we will not break palindrome property.

# What happens, if we reached the last element and were not able to apply strategy above? Then we have string like this aaaaaa..aaaaaa or aaaaaa...z...aaaaaa, where z can be any symbol. In this case to get the smalles string as possible we need to replace last symbol to "b". Also there is case when n = 1, and we can not break palindrome property so we return "".
        size=len(s)
        if size==1:
            return ""
        for i in range(size//2):
            if s[i]!="a":
                return s[:i]+'a'+s[i+1:]
        return s[:-1]+'b'