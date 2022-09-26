import collections
class Solution:
    def isValidSudoku(self, board: list[list[str]]) -> bool:
    # Defaultdict is a container like dictionaries present in the module collections. Defaultdict is a sub-class of the dictionary class that returns a dictionary-like object. The functionality of both dictionaries and defaultdict are almost same except for the fact that defaultdict never raises a KeyError. It provides a default value for the key that does not exists.
        rows=collections.defaultdict(set)
        column=collections.defaultdict(set)
        square=collections.defaultdict(set)
        for row in range(9):
            for col in range(9):
                curElem=board[row][col]
                if curElem==".":
                    continue
                if  curElem in rows[row] or curElem in column[col] or curElem in square[(row//3,col//3)]:
                        return False
                rows[row].add(curElem)
                column[col].add(curElem)                             
                square[(row//3,col//3)].add(curElem)
        return True