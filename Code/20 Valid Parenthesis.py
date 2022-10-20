class stack:
    def __init__(self):
        self.arr = []

    def push(self, data):
        self.arr.append(data)

    def pop(self):
        self.arr.pop()

    def isEmpty(self):
        return True if len(self.arr) == 0 else False


class Solution:
    def isValid(self, s: str) -> bool:
        s1 = []
        Map = {")": "(", "]": "[", "}": "{"}
        for i in s:
            #           when i is a closing bracket
            if i in Map:
                if s1 and s1[-1] == Map[i]:
                    s1.pop()
                else:
                    return False
#           when i is a opening bracket
            else:
                s1.append(i)
        return True if len(s1) == 0 else False
