class Solution:
    def findMin(self, arr: List[int]) -> int:
        low = 0
        high = len(arr)-1
        Min = arr[0]
        while low <= high:
            #             if the portion is sorted return the min of sorted portion and current minimum
            if arr[low] < arr[high]:
                Min = min(Min, arr[low])
                break
            mid = (low+high)//2
            Min = min(Min, arr[mid])
            if arr[mid] >= arr[low]:
                #                 search in right portion
                low = mid+1
            else:
                #                 search in left portion
                high = mid-1
        return Min
