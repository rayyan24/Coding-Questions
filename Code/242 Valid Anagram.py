class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        sizeS, sizeT = len(s), len(t)
        if sizeS != sizeT:
            return False
        mapS, mapT = {}, {}
#       key -> character value -> counter
        for i in range(sizeS):
            mapS[s[i]] = 1+mapS.get(s[i], 0)
            mapT[t[i]] = 1+mapT.get(t[i], 0)
        for i in mapS:
            if mapS.get(i) != mapT.get(i, 0):
                return False
        return True
