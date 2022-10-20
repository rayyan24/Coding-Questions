class Solution:
    def maxSubArray(self, arr: List[int]) -> int:
        MaxSum = arr[0]
        curSum = 0
        for i in arr:
            if curSum < 0:
                curSum = 0
            curSum += i
            MaxSum = max(MaxSum, curSum)
        return MaxSum
