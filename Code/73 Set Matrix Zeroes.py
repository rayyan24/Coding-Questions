class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        rowZero = False  # to check if we want to make row 0 to all zeros
        rows, cols = len(matrix), len(matrix[0])
        for r in range(rows):
            for c in range(cols):
                if matrix[r][c] == 0:
                    matrix[0][c] = 0  # set 0 on the 0 row of current column
                    if r == 0:
                        rowZero = True
                    else:
                        # set 0 on the 0 column of current row
                        matrix[r][0] = 0
        for r in range(1, rows):
            for c in range(1, cols):
                if matrix[0][c] == 0 or matrix[r][0] == 0:
                    matrix[r][c] = 0
#         setting first column to zero
        if matrix[0][0] == 0:
            for r in range(rows):
                matrix[r][0] = 0
        if rowZero == True:
            for c in range(cols):
                matrix[0][c] = 0
