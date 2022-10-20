class Solution:
    def sortColors(self, nums: List[int]) -> None:
        Zeros = 0
        Ones = 0
        Twos = 0
        for i in nums:
            if i == 0:
                Zeros += 1
            elif i == 1:
                Ones += 1
            else:
                Twos += 1
        a = [0]*Zeros+[1]*Ones+[2]*Twos
        for i in range(len(nums)):
            nums[i] = a[i]
