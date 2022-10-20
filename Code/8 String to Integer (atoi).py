class Solution:
    def myAtoi(self, s: str) -> int:
        s = s.strip()
#       to check if s is an empty string
        if not s:
            return 0
        Max=2**31 - 1
        Min=-2**31
        sign = -1 if s[0] == '-' else 1
        if s[0] in {'-', '+'}:
            s = s[1:]
        num = 0
        for c in s:
#         if the current char is not a number all the other numbers after that character will be skipped
            if not c.isdigit():
                break
            num = num * 10 + int(c)
            if sign * num <= Min:
                return Min
            if sign * num >= Max:
                return Max
        return sign * num