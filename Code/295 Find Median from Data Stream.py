# 295 Find Median from Data Stream
from sortedcontainers import SortedList
class MedianFinder:
    def __init__(self):
        self.arr=SortedList()
        self.count=0

    def addNum(self, num: int) -> None:
        self.arr.add(num)
        self.count+=1

    def findMedian(self) -> float:
#       even
        if self.count%2==0:
            mid=self.count//2
            return (self.arr[mid-1]+self.arr[mid])/2
#	odd
        else:
            return self.arr[self.count//2]