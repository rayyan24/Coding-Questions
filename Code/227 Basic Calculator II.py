class Solution:
    def calculate(self, s: str) -> int:
        s=s.replace(" ","")
        res=0 # stores previously computed values excluding prevNUM and curNum
        lastNum=0
        curNum=0
        operand="+"
        for char in s+"+":
            if char.isdigit():
                curNum=10*curNum+int(char)
                continue
            if operand=="+":
                res+=lastNum
                lastNum=curNum
            elif operand=="-":
                res+=lastNum
                lastNum=-curNum
            elif operand=="*":
                lastNum*=curNum
            elif operand=="/":
                lastNum=int(lastNum/curNum)
            operand=char
            curNum=0
        return res+lastNum