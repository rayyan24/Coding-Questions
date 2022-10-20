class Solution:
    def twoSum(self, arr: List[int], target: int) -> List[int]:

        #         for i in range(size):
        #             for j in range(i+1,size):
        #                 if arr[i]+arr[j]==target:
        #                     return [i+1,j+1]
        #                 elif arr[i]+arr[j]>target:
        #                     break
        #         return[]
        # for i in range(size):
        #     reqVal=target-arr[i]
        #     low=0
        #     high=size-1
        #     while(low<=high):
        #         mid=(low+high)//2
        #         if arr[mid]==reqVal:
        #             return[i+1,mid+1]
        #         elif(reqVal<arr[mid]):
        #             high=mid-1
        #         else:
        #             low=mid+1

        size = len(arr)
        left = 0
        right = size-1
        while left <= right:
            curSum = arr[left]+arr[right]
            if curSum == target:
                return [left+1, right+1]
            elif curSum > target:
                right -= 1
            else:
                left += 1
