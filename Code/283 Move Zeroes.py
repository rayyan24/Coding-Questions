# class Solution:
#     def moveZeroes(self, arr: List[int]) -> None:
#         numArr=[0 for i in arr]
#         count=0
#         for i in range(len(arr)):
#             if arr[i]!=0:
#                 numArr[count]=arr[i]
#                 count+=1     
#         for i in range(len(arr)):
#             arr[i]=numArr[i]

class Solution:
      def moveZeroes(self, nums: List[int]) -> None:
        j = 0
        for num in nums:
            if num != 0:
                nums[j] = num
                j += 1
        for i in range(j, len(nums)):
             nums[i] = 0