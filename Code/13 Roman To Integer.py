class Solution:
    def romanToInt(self, roman: str) -> int:
        map = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}
        size = len(roman)
        integer = 0
        for i in range(size):
            curElem = map.get(roman[i])
            nextElem = map.get(roman[i+1]) if (i+1) < size else 0
#           when current element is less than next element subtract current element
            if curElem < nextElem:
                integer -= curElem
            else:
                integer += curElem

        return integer
