import heapq
a=[1,6,44,77,54,6,454,6,23,32]
a=list(map(lambda x:-x,a))
heapq.heapify(a)
print(a)
heapq.heappop(a)
print(a)
'''
1962. Remove Stones to Minimize the Total
Medium

minheap minimum element at the top
maxheap maximum element at the top
'''
class Solution:
    def minStoneSum(self, piles: List[int], k: int) -> int:
        # changes the sign of whole array to simulate a max heap
        piles=list(map(lambda x:-x,piles))
        heapq.heapify(piles)
        for i in range(k):
            # - is used to change the sign so that we can use it as a max heap
            # use - only where we are using any function of heapq
            currentMax=-heapq.heappop(piles)
            canRemove=currentMax//2
            newElem=currentMax-canRemove
            heapq.heappush(piles,-newElem)
        return sum(piles)*-1