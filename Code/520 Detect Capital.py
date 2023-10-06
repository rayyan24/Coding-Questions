class Solution:
    def detectCapitalUse(self, w: str) -> bool:
        up = low = 0
        for c in w:
            if c.isupper():
                up += 1
            else:
                low += 1
        return up==len(w) or low==len(w) or (up==1 and w[0].isupper())