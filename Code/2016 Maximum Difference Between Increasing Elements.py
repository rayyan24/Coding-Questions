class Solution:
    def maximumDifference(self, nums: List[int]) -> int:
        maxdiff = -1
        # i,j=0,1
        # while j<len(nums):
        #     if (nums[j]-nums[i])>maxdiff:
        #         maxdiff=nums[j]-nums[i]
        #     j+=1
        #     i+=1
        for i in range(len(nums)):
            for j in range(i+1, len(nums)):
                curDiff = nums[j]-nums[i]
                if curDiff > maxdiff:
                    maxdiff = curDiff
        return maxdiff if maxdiff != 0 else -1
