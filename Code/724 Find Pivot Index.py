class Solution:
    def pivotIndex(self, arr: List[int]) -> int:
        for i in range(len(arr)):
            before = sum(arr[0:i])
            after = sum(arr[i+1:])
            if before == after:
                return i
        return -1
