class Solution:
    def myPow(self, base: float, exp: int) -> float:
        # if exp<0:
        #     exp*=-1
        #     result=1
        #     for i in range(exp):
        #         result*=base
        #     return 1/result
        # else:
        #     result=1
        #     for i in range(exp):
        #         result*=base
        #     return result
        def helper(x,n):
            if x==0:
                return 0
            if n==0:
                return 1
            res=helper(x*x,n//2)
            return x*res if n%2 else res
        res=helper(base,abs(exp))
        return res if exp>=0 else 1/res
        # return base**exp
            
            