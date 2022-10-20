class Solution:
    def isMonotonic(self, arr: List[int]) -> bool:
        size = len(arr)
        if arr[0] == arr[size-1]:
            for i in range(size-1):
                if arr[i] != arr[0]:
                    return False
        elif (arr[0] < arr[size-1]):
            for i in range(size-1):
                if arr[i] > arr[i+1]:
                    return False
        else:
            for i in range(size-1):
                if arr[i] < arr[i+1]:
                    return False
        return True
