class Solution:
    def minDifficulty(self, arr: List[int], d: int) -> int:
        size=len(arr)
#         jobs are less days are more
        if size<d:
            return -1
        MAX=sys.maxsize
        @lru_cache(None) # for memoization 
        def helper(curInd,remDays):
            if remDays==0:
                if curInd==size:
                    return 0
                else:
                    return MAX
            if curInd==size:
                if remDays==0:
                    return 0
                else:
                    return MAX
            ans=sys.maxsize
            curMax=0
            for i in range(curInd,size):
                curMax=max(curMax,arr[i])
                ans=min(ans,curMax+helper(i+1,remDays-1))
            return ans
        return helper(0,d)
        
        