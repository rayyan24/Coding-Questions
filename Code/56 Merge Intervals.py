class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        # print(intervals)
        intervals.sort()
        print(intervals)  # [[1, 3], [2, 6], [8, 10], [15, 18]]
        res = [intervals[0]]
        for start, end in intervals[1:]:
            lastEnd = res[-1][1]  # result ke last element ki upper limit
            if start <= lastEnd:
                res[-1][1] = max(lastEnd, end)
            else:
                res.append([start, end])
        return res
