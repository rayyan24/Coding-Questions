class Solution:
    def isUgly(self, n: int) -> bool:
        # keep dividing the number by 2,3,5 if after division the number reaches 1 it is an ugly number else it is not an ugly number
        def check(i):
            nonlocal n
            while n%i==0:
                n//=i
        if n<=0:
            return False
        check(2)
        check(3)
        check(5)
        return n==1