class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        def toNum(s):
            num = 0
            for char in s:
                # converts char to number
                num = num*10+ord(char)-48
            return num
        num1 = toNum(num1)
        num2 = toNum(num2)
        res = str(num1*num2)
        return res
