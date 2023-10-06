class Solution:
    def getOrder(self, tasks: List[List[int]]) -> List[int]:
        for ind,val in enumerate(tasks):
            val.append(ind)
        '''tasks[i][0] --> Enqueue Time
           tasks[i][1] --> Processing Time
           tasks[i][2] --> Orignal Index
        '''
        tasks.sort(key=lambda x:x[0]) #Sort According to Arrival Time
        res=[]
        heap=[]# Min Heap
        i=0
        time=tasks[0][0] # the time we are currently at
        size=len(tasks)
        while heap or i<size:
            while i<size and time>=tasks[i][0]:
                heapq.heappush(heap,[tasks[i][1],tasks[i][2]])
                i+=1
            if not heap:
                time=tasks[i][0] # setting the time to next arrival time to skip ideal time
            else:
                pTime,index=heapq.heappop(heap)
                time+=pTime
                res.append(index) 
        return res