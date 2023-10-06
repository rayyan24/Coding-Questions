class Solution:
    def closestMeetingNode(self, edges: List[int], node1: int, node2: int) -> int:
        def helper(node):
            visited,i,dist={},node,0
            while i not in visited and i!=-1:
                visited[i]=dist
                i=edges[i]
                dist+=1
            return visited
        vis1,vis2=helper(node1),helper(node2)
        commonNodes = set(list(vis1.keys())).intersection(set(list(vis2.keys())))
        Min,resIndex=float(inf),-1
        for i in commonNodes:
            curMin=max(vis1[i],vis2[i])
            if curMin<Min:
                resIndex=i
                Min=curMin
            elif curMin==Min and i<resIndex:
                resIndex=i
        return resIndex