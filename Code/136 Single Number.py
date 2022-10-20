class Solution:
    def singleNumber(self, arr: List[int]) -> int:
        res = 0
        for i in arr:
            res = res ^ i
        return res
