class Solution:
    def rearrangeArray(self, nums: List[int]) -> List[int]:
        ind_pos=0
        ind_neg=1
        res=[0]*len(nums)
        for CE in nums:
#             when current number is positive
            if CE>0:
                res[ind_pos]=CE
                ind_pos+=2
            # when CE is negative
            if CE<0:
                res[ind_neg]=CE
                ind_neg+=2
        return res
                
            