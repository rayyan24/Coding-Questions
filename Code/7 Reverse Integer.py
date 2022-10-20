class Solution:
    def reverse(self, num: int) -> int:
        # if (x<-2**31) or (x>=(2**31)-1):
        #     return 0
        # sign=1
        # x=str(x)
        # x=x[::-1]
        # if x[-1]=="-":
        #     x=x.replace("-","")
        #     sign=-1
        # x=int(x)
        # return (x*sign)
        sign = 1
        if num < 0:
            sign = -1
        num = str(num)
        num = num.replace("-", "")
        num = num[::-1]
        num = int(num)
        if (num < -2**31) or (num >= (2**31)-1):
            return 0
        else:
            return num*sign
