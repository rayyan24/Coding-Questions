# """
# This is the interface that allows for creating nested lists.
# You should not implement it, or speculate about its implementation
# """
#class NestedInteger:
#    def isInteger(self) -> bool:
#        """
#        @return True if this NestedInteger holds a single integer, rather than a nested list.
#        """
#
#    def getInteger(self) -> int:
#        """
#        @return the single integer that this NestedInteger holds, if it holds a single integer
#        Return None if this NestedInteger holds a nested list
#        """
#
#    def getList(self) -> [NestedInteger]:
#        """
#        @return the nested list that this NestedInteger holds, if it holds a nested list
#        Return None if this NestedInteger holds a single integer
#        """
#  ***************341. Flatten Nested List Iterator********************
class NestedIterator:
    def __init__(self, List: [NestedInteger]):
        self.arr=[]
        self.curInd=0
        def helper(nestedList):
            for CE in nestedList:
                if CE.isInteger():
                    self.arr.append(CE.getInteger())
                else:
                    helper(CE.getList())
        helper(List)
        
    def next(self) -> int:
        self.curInd+=1
        return self.arr[self.curInd-1]
    
    def hasNext(self) -> bool:
        return self.curInd<len(self.arr)