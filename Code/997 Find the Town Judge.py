class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        if not trust and n == 1: 
            return 1
        count = [0] * (n + 1)
        # the person who trusts get decremented
        # the person who is trusted gets incremented
        for i,j in trust:
            # i trusts j
            count[i] -= 1
            count[j] += 1
        for ind,val in enumerate(count):
            if val == n - 1: 
                return ind
        return -1