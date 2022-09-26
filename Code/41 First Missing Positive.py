class Solution:
    def firstMissingPositive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums)<10000:
            i=1
            while True:
                if i not in nums:
                    return i
                    break
                else:
                    i+=1
        else:
            return len(nums)+1
        
class Solution:
    def firstMissingPositive(self, arr):
        size=len(arr)
        for i in range(size):
            if arr[i]<0:
                arr[i]=0
        for i in range(size):
            val=abs(arr[i])
            if 1<=val<=size:
                if arr[val-1]>0:
                    arr[val-1] *= -1
                elif arr[val-1] == 0:
                    arr[val-1] = -1*(size+1)
        for i in range(1,size+1):
            if arr[i-1]>=0:
                return i
        return size+1

                
                
                
                
                
                
                
                
                
                
                
                
                
                
                
                
                
                
        