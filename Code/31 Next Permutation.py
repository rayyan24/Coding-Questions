# **************31. Next Permutation*************
class Solution:
    def nextPermutation(self, arr: List[int]) -> None:
        def reverse(nums,start,end):
            while start<end:
                nums[start],nums[end]=nums[end],nums[start]
                start+=1
                end-=1
        toSwap1=-1
        size=len(arr)
        for i in range(size-1,0,-1):
# when current element is greater than previous element then previous element is the first number which is to be swapped
            if arr[i]>arr[i-1]: 
                toSwap1=i-1
                break
# when toSwap1 is -1 means array is sorted in descending order reverse array and return 
        if toSwap1==-1:
            reverse(arr,0,size-1)
            return
# loop fron end to toSwap1 and find a greater element than arr[toswap1]
        toSwap2=size-1
        for i in range(size-1,toSwap1,-1):
             if arr[i]>arr[toSwap1]:
                toSwap2=i
                break
        print(arr[toSwap1],arr[toSwap2])
        arr[toSwap1],arr[toSwap2]=arr[toSwap2],arr[toSwap1]
        reverse(arr,toSwap1+1,size-1)