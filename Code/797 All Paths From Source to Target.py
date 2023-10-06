'''
797. All Paths From Source to Target
Medium

Given a directed acyclic graph (DAG) of n nodes labeled from 0 to n - 1, find all possible paths from node 0 to node n - 1 and return them in any order.

The graph is given as follows: graph[i] is a list of all nodes you can visit from node i (i.e., there is a directed edge from node i to node graph[i][j]).
'''
class Solution:
    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
        size=len(graph)#number of nodes in graph
        res=[]
        def helper(ind,curPath):
            if ind==size-1:
                res.append(curPath[:])
                return
            for i in graph[ind]:
                helper(i,curPath+[i])
        helper(0,[0])
        return res