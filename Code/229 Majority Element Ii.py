class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        arr = set(nums)
        arr = list(arr)
        result = []
        for i in arr:
            if nums.count(i) > len(nums)//3:
                result.append(i)
        return result
