class Solution:
    def closeStrings(self, word1: str, word2: str) -> bool:
# create an array where occurances of a are at 0 index b at 1 index and so on
# check if both the arrays have same frequency or not
# sort them and retuen if they are equal or not

        def helper(word):
            res=[0]*26
            for char in word:
                res[ord(char)-97]+=1
            return (res)
        w1=helper(word1)
        w2=helper(word2)
        for i in range(26):
            if (w1[i]==0 and w2[i]!=0) or (w1[i]!=0 and w2[i]==0):
                return False
        w1.sort()
        w2.sort()
        return w1==w2