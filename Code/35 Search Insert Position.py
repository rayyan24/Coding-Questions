class Solution:
    def searchInsert(self, arr: List[int], target: int) -> int:
        low = 0
        high = len(arr)-1
        while (low <= high):
            mid = (low+high)//2
            if (arr[mid] == target):
                return mid
            elif (target < arr[mid]):
                high = mid-1
            else:
                low = mid+1
        if target < arr[mid]:
            return mid
        else:
            return mid+1
