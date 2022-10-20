class Solution:
    def maxFrequency(self, arr: List[int], k: int) -> int:
        l = 0
        r = 0
        total = 0
        res = 0
        arr.sort()
#         size of sliding window is (r-l+1)
        while r < len(arr):
            total += arr[r]
            while arr[r]*(r-l+1) > total+k:
                total -= arr[l]
                l += 1
            res = max(res, (r-l+1))
            r += 1
        return res
