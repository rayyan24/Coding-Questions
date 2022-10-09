class Solution:
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        firstRow=matrix[0]
        for r in matrix[1:]:
            for c in r:
                firstRow.append(c)
        firstRow.sort()       
        return firstRow[k-1]