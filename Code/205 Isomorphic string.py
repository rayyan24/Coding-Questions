class Solution:
    def isIsomorphic(self, s1: str, s2: str) -> bool:
        ST, TS = {}, {}
        for i, j in zip(s1, s2):
            if (i in ST and ST[i] != j) or (j in TS and TS[j] != i):
                return False
            ST[i] = j
            TS[j] = i

        return True
