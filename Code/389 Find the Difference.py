class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        Count=Counter(t)
        for char in s:
            Count[char]-=1
        for char,count in Count.items():
            if count!=0:
                return char