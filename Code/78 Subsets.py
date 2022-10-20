class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        temp = []
        ans = []

        def helper(index):
            if index >= len(nums):
                ans.append(temp.copy())
                return
#           chosing the i th element
            temp.append(nums[index])
            helper(index+1)
#         not chosing the i th element
            temp.pop()
            helper(index+1)
        helper(0)
        return ans
