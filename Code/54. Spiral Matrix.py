def showMatrix(matrix) -> None:
    for row in matrix:
        print(*row)
    print()

# https://leetcode.com/problems/spiral-matrix/discuss/20571/1-liner-in-Python-%2B-Ruby
a = [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]]
# 54. Spiral Matrix
# Given an m x n matrix, return all elements of the matrix in spiral order.


class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        res = []
        while matrix:
            #           extract the first row from the matrix
            res.extend(matrix.pop(0))
#           rotate the remaining matrix anti-clockwise
            matrix = [*zip(*matrix)][::-1]
        return res
