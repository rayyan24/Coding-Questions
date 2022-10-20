class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        Sum=sum(nums)
        if Sum%2:
            return False
        SUMS=set()
        SUMS.add(0)
        target=Sum/2
        for i in nums:
            temp=set()
            for j in SUMS:
                if i+j==target:
                    return True
                temp.add(j+i)
                temp.add(j)
            SUMS=temp
        
        return False
            