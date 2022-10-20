class Solution:
    def runningSum(self, arr: List[int]) -> List[int]:
        runningSum = [0 for i in arr]
        size = len(arr)
        runningSum[0] = arr[0]
        for i in range(1, size):
            runningSum[i] = arr[i]+runningSum[i-1]
        return runningSum
