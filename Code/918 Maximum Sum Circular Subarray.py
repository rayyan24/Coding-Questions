class Solution:
    def maxSubarraySumCircular(self, nums: List[int]) -> int:
        totalSum=0
        maxSum,curMax=nums[0],0
        minSum,curMin=nums[0],0
        for el in nums:
            curMax=max(curMax+el,el)
            maxSum=max(maxSum,curMax)

            curMin=min(curMin+el,el)
            minSum=min(minSum,curMin)

            totalSum+=el
        if maxSum>0:
            return max(maxSum,totalSum-minSum)
        else:
            return maxSum