class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        temp = []
        ans = []

        def helper(Open, Closed):
            #             case when we got a valid arrangement
            if Open == Closed == n:
                ans.append("".join(temp))
                return
#             when we can add a opening bracket
            if Open < n:
                temp.append("(")
                helper(Open+1, Closed)
                temp.pop()
#             when we can add a closing bracket
            if Closed < Open:
                temp.append(")")
                helper(Open, Closed+1)
                temp.pop()
        helper(0, 0)
        return ans
