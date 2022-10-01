class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        
        for i in range(len(arr)-1):
            arr[i]=max(arr[i+1:])
        arr[-1]=-1
        return arr
#Iterate from the back to the start,
#We initilize mx = -1, where mx represent the max on the right.
#Each round, we set A[i] = mx, where mx is its mas on the right.
#Also we update mx = max(mx, A[i]), where A[i] is its original value