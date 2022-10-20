class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        res=""
        FE=strs[0]
        for i,char in enumerate(FE):
            for s in strs:
                if i==len(s) or s[i]!=char:
                    return res
# if this loop did not terminate means char is present in all the strings and can be added to result
            res+=char
        return res