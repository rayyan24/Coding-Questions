class Solution:
    def addDigits(self, n: int) -> int:
        while True:
            n = sum([int(i) for i in str(n)])
            if n >= 0 and n <= 9:
                break
        return n
