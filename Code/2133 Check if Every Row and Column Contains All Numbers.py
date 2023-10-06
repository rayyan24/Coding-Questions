class Solution:
    def checkValid(self, matrix: List[List[int]]) -> bool:
        n = len(matrix)
        for i in range(n):
            dic1 = {}
            dic2 = {}
            for j in range(n):
                if matrix[i][j] not in dic1:
                    dic1[matrix[i][j]] = 1
                else:
                    return False
                if matrix[j][i] not in dic2:
                    dic2[matrix[j][i]] = 1
                else:
                    return False
        return True