class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        # for i in range(len(nums)):
        #     if nums[i]==val:
        #         del nums[i]
        # print(nums
        #      )
        i = 0
        while (i < len(nums)):
            if nums[i] == val:
                del nums[i]
            i += 1
        i = 0
        while (i < len(nums)):
            if nums[i] == val:
                del nums[i]
            i += 1
