# 931. Minimum Falling Path Sum
class Solution:
    def minFallingPathSum(self, arr: List[List[int]]) -> int:
        n=len(arr)
        for row in range(1,n):
            for col in range(n):
                if col==0:
                    arr[row][col]=arr[row][col]+min(arr[row-1][col],arr[row-1][col+1])
                elif col==n-1:
                    arr[row][col]=arr[row][col]+min(arr[row-1][col],arr[row-1][col-1])
                else:
                    arr[row][col]=arr[row][col]+min(arr[row-1][col],arr[row-1][col-1],arr[row-1][col+1])
        return min(arr[n-1])