class Solution:
    def trap(self, arr: List[int]) -> int:
        size=len(arr)
        if size==0:
            return 0
        left=0
        right=size-1
        leftMax=arr[left]
        rightMax=arr[right]
        res=0
        while left<right:
#       shift the pointer which is smaller
            if leftMax<rightMax:
                left+=1
                leftMax=max(leftMax,arr[left])
                res+=leftMax-arr[left]
            else:
                right-=1
                rightMax=max(rightMax,arr[right])
                res+=rightMax-arr[right]
        return res