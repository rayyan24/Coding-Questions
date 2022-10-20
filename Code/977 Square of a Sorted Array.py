class Solution:
    def sortedSquares(self, arr: List[int]) -> List[int]:
        start = 0
        end = len(arr)-1
        i = len(arr)-1
        squareArray = [0 for i in range(len(arr))]
        # squareArray=[0]*(len(arr)-1)
        while (i >= 0):
            if arr[start]**2 > arr[end]**2:
                squareArray[i] = arr[start]**2
                start += 1
            else:
                squareArray[i] = arr[end]**2
                end -= 1
            i -= 1
        return (squareArray)
