class Solution:
    def threeSum(self, arr: List[int]) -> List[List[int]]:
        res = []
        arr.sort()
        for index, val in enumerate(arr):
            if index > 0 and val == arr[index-1]:
                continue
            left, right = index+1, len(arr)-1
            while left < right:
                Sum = val+arr[left]+arr[right]
                if Sum > 0:
                    right -= 1
                elif Sum < 0:
                    left += 1
                else:
                    res.append([val, arr[left], arr[right]])
                    left += 1
                    while arr[left] == arr[left-1] and left < right:
                        left += 1
        return res
