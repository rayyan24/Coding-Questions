# class Solution:
#     def dailyTemperatures(self, arr: List[int]) -> List[int]:
# #         size=len(arr)
# #         res=[0]*size
# #         for ind,val in enumerate(arr):
# #             for j in range(ind+1,size):
# #                 if arr[j]>arr[ind] and res[ind]==0:
# #                     res[ind]=j-ind
# #         return res
#         res=[0]*len(arr)
#         stack=[]
#         # ind will be ahead of stackInd
#         for ind,val in enumerate(arr):
#             while stack and val>stack[-1][0]:
#                 stackVal,stackInd=stack.pop()
#                 res[stackInd]=ind-stackInd
#             stack.append([val,ind])
#         return res

class Solution:
      def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        ans = [0] * len(temperatures)
        stack = []

        for curIndex, curTemp in enumerate(temperatures):
            while stack and curTemp > temperatures[stack[-1]]:
                index = stack.pop()
                ans[index] = curIndex - index
            stack.append(curIndex)

        return ans