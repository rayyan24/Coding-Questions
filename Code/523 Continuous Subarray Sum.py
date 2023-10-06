class Solution:
    def checkSubarraySum(self, arr: List[int], k: int) -> bool:
        # ********* Also A Solution*************
        # def isMultiple(num):
        #     if num%k==0:
        #         return True
        #     return False
        # size=len(arr)
        # for left in range(size):
        #     right=left+1
        #     while right<size:
        #         Sum=sum(arr[left:right+1])
        #         if isMultiple(Sum):
        #             return True
        #         right+=1
        # return False
        
#       elemenate a edge case when there are two or more consecutive zeros 
        Map={0:-1} #key-> remainder value->index
        Sum=0
        for index,value in enumerate(arr):
            Sum+=value
            remainder=Sum%k
            # if Map already has a value with a same remainder it means a multiple of k must have been added to the total
            if remainder not in Map:
                Map[remainder]=index
            # when Map contains the remainder second condition to check if the sub-array have atleast 2 elements 
            elif index-Map[remainder]>1:
                return True
        return False
            
                
            
            
            
            
            
            
            
            
            