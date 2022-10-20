class Solution:
    def addBinary(self, a: str, b: str) -> str:
        a, b = a[::-1], b[::-1]
        LA, LB = len(a), len(b)
        carry = 0
        res = ""
        for i in range(max(LA, LB)):
            #             48 is the ascii value of 0 this converts the binary number to decimal
            digitA = ord(a[i])-48 if i < LA else 0
            digitB = ord(b[i])-48 if i < LB else 0

            total = digitA+digitB+carry
            char = str(total % 2)
            res = char+res
            carry = total//2
#         check if carry is 1 after completion if yes ten add one more 1 in res
        if carry:
            res = "1"+res
        return res
