class Solution:
    def search(self, arr: List[int], target: int) -> int:
        low = 0
        high = len(arr)-1
        while (low <= high):
            mid = (low+high)//2
            if (arr[mid] == target):
                return mid
#             when left side of mid is strictly increasing
            elif (arr[mid] >= arr[low]):
                if target <= arr[mid] and target >= arr[low]:
                    high = mid-1
                else:
                    low = mid+1
            # when left side of mid is strictly increasing
            else:
                if target >= arr[mid] and target <= arr[high]:
                    low = mid+1
                else:
                    high = mid-1
        return -1
