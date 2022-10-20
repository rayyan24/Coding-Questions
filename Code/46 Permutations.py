class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        ans = []

        if len(nums) == 1:
            return [nums[:]]
        for i in range(len(nums)):
            #             removes element at 0 index
            remElmnt = nums.pop(0)
            otherPerms = self.permute(nums)
            for i in otherPerms:
                i.append(remElmnt)
#             appends all the elements in otherPerms to ans
            ans.extend(otherPerms)
            nums.append(remElmnt)
        return ans
