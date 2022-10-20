class Solution:
    def searchRange(self, arr: List[int], target: int) -> List[int]:
        low = 0
        high = len(arr)-1
        while (low <= high):
            mid = (low+high)//2
            if (arr[mid] == target):
                start = mid
                end = mid
                while start >= 0 and arr[start] == target:
                    start -= 1
                while end < len(arr) and arr[end] == target:
                    end += 1
#                 start+1 and end -1 because the loop will run on extra t
                return [start+1, end-1]
            elif (target < arr[mid]):
                high = mid-1
            else:
                low = mid+1
        return [-1, -1]
