class Solution:
    def maxPoints(self, points: List[List[int]]) -> int:
        # using a slope and intercept to identify a line and add all the points that passes through that line 
        def helper(x0,y0,x1,y1):
            if y0==y1:
                slope,intercept=0,y0
            elif x0==x1:
                slope,intercept=x0,None
            else:
                slope=(y1-y0)/(x1-x0)
                intercept=y0-slope*x0
            return slope,intercept
        size=len(points)
        if size==1:
            return 1
        Map=defaultdict(set)
        for i in range(size):
            for j in range(i+1,size):
                x0,y0=points[i]
                x1,y1=points[j]
                line=helper(x0,y0,x1,y1)
                Map[line].add(i)
                Map[line].add(j)
        return max([len(Map[line]) for line in Map])