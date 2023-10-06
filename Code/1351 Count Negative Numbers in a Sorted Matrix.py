class Solution:
    def countNegatives(self, grid: List[List[int]]) -> int:
        rows=len(grid)
        columns=len(grid[0])
        count=0
        for i in range(rows):
            for j in range(columns):
                if grid[i][j]<0:
                    count+=1
        return count