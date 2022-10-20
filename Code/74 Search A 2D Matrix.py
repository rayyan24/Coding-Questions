class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        for i in range(len(matrix)):
            if target >= matrix[i][0] and target <= matrix[i][-1]:
                break
        for j in matrix[i]:
            if j == target:
                return 1
        return 0
