class Solution:
    def shortestAlternatingPaths(self, n, redEdges, blueEdges):
        redAdjList=collections.defaultdict(list)
        blueAdjList=collections.defaultdict(list)
        for src,dest in redEdges:
            redAdjList[src].append(dest)
        for src,dest in blueEdges:
            blueAdjList[src].append(dest)
        res=[-1]*n
        queue=deque()
        queue.append([0,0,None]) #[node,distance,color]
        visited=set()
        visited.add((0,None))# (node,color)
        while queue:
            node,dist,edgeColor=queue.popleft()
            if res[node]==-1:
                res[node]=dist
            if edgeColor!= "RED":
                for i in redAdjList[node]:
                    if (i,"RED") not in visited:
                        visited.add((i,"RED"))
                        queue.append([i,dist+1,"RED"])
            if edgeColor!= "BLUE":
                for i in blueAdjList[node]:
                    if (i,"BLUE") not in visited:
                        visited.add((i,"BLUE"))
                        queue.append([i,dist+1,"BLUE"])
        return res