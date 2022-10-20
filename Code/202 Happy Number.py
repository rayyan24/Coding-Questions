class Solution:
    def isHappy(self, n: int) -> bool:
        Set = set()
        while n != 1:
            n = sum([int(i)**2 for i in str(n)])
            if n in Set:
                return False
            else:
                Set.add(n)
        return True
