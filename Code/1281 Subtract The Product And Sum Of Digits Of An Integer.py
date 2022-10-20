class Solution:
    def subtractProductAndSum(self, n: int) -> int:

        Sum = 0
        product = 1
        # while n>:
        #     Sum+=n%10
        #     product*=n%10
        #     n=n%10
        for i in str(n):
            Sum += int(i)
            product *= int(i)
        return product-Sum
