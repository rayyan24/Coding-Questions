class Solution:
    def addToArrayForm(self, num: List[int], k: int) -> List[int]:
        Num = 0
        for i in num:
            Num = 10*Num+int(i)
        return [i for i in str(Num+k)]
