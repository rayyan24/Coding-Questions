s = "123"
res = 0
for i in s:
    curChar = ord(i)-ord("0")
    res = 10*res+curChar
print(res)
print(ord("0"))
print(ord("4")-48)


class Solution:
    def myAtoi(self, s: str) -> int:
        s = s.strip()
        #    to check if s is an empty string
        if not s:
            return 0
        Max = 2**31 - 1
        Min = -2**31
        sign = -1 if s[0] == '-' else 1
        if s[0] in {'-', '+'}:
            s = s[1:]
        num = 0
        for c in s:
            # if the current char is not a number all the other numbers after that character will be skipped
            if not c.isdigit():
                break
            # ascii value of 0 is 48
            num = num * 10 + ord(c) - 48
            if sign * num <= Min:
                return Min
            if sign * num >= Max:
                return Max
        return sign * num
