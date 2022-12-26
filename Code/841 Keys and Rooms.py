# 841. Keys and Rooms Medium
class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        visited=set()
        adjList=defaultdict(list)
        def dfs(start):
            if start not in visited:
                visited.add(start)
                for i in adjList[start]:
                    dfs(i)
        for ind,val in enumerate(rooms):
            adjList[ind].extend(val)
        dfs(0)
        return len(visited)==len(rooms)