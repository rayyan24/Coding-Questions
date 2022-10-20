class Solution:
    def minimumTotal(self, arr: List[List[int]]) -> int:
        # res=[]
        # for row in arr:
        #     res.append(min(row))
        # return sum(res)
        res = [0]*(len(arr)+1)
        for row in arr[::-1]:
            for i, value in enumerate(row):
                res[i] = value+min(res[i], res[i+1])
        return res[0]
