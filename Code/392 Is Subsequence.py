class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        i, j = 0, 0
        len_s = len(s)
        while (i != len_s and j != len(t)):
            if s[i] == t[j]:
                i += 1
            j += 1
        if i == len_s:
            return True
        return False
