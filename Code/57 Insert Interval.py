class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        def mergeIntervals():
            res=[intervals[0]]
            for start,end in intervals[1:]:
                lastEnd=res[-1][1]# end val of last element of result
                if start<=lastEnd:
                    res[-1][1]=max(lastEnd,end)
                else:
                    res.append([start,end])
            return res
        insertIndex=len(intervals)
        for ind,val in enumerate(intervals):
            if val[0]>=newInterval[0]:
                insertIndex=ind
                break
        intervals.insert(insertIndex,newInterval)
        res=mergeIntervals()
        return res
