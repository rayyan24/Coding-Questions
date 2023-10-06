class Solution:
    def findSubsequences(self, nums: List[int]) -> List[List[int]]:
        res=set()
        size=len(nums)
        def helper(i,curSubseq):
            if i==size:
                if len(curSubseq)>1:
                    res.add(tuple(curSubseq))
                return
            if len(curSubseq)==0 or curSubseq[-1]<=nums[i]:
                helper(i+1, curSubseq+[nums[i]] )
            helper(i+1,curSubseq)
        helper(0,[])
        return res