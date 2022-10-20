class Solution:
    def numberOfSteps(self, num: int) -> int:
        def helper(n, step=0):
            if n == 0:
                return step
#             even
            elif (n % 2 == 0):
                return helper(n//2, step+1)
#             odd
            else:
                return helper(n-1, step+1)
        return helper(num)
