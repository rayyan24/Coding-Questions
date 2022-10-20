class Solution:
    def findDiagonalOrder(self, matrix: List[List[int]]) -> List[int]:
        d = {}
        for i in range(len(matrix)):
            for j in range(len(matrix[i])):
                # if no entry in dictionary for sum of indices aka the diagonal, create one
                if i + j not in d:
                    d[i+j] = [matrix[i][j]]
                else:
                    # If you've already passed over this diagonal, keep adding elements to it!
                    d[i+j].append(matrix[i][j])
        ans = []

        # in  d.items() [0] sum of indexes is present
        # in  d.items() [1] values at sum of the indexes

        for item in d.items():
            # if sum of indexes is even add in revese order
            if item[0] % 2 == 0:
                [ans.append(x) for x in item[1][::-1]]
            else:
                [ans.append(x) for x in item[1]]
        return ans
