class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        for x in nums.copy():
            if nums.count(x) > 1:
                nums.remove(x)
        return len(nums)
