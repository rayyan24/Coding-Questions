from collections import Counter
List = list


class Solution:
    def findErrorNums(self, arr: List[int]) -> List[int]:
        frequency = Counter(arr)
        res = []
        size = len(arr)
        for value, freq in frequency.items():
            if freq > 1:
                res.append(value)
        for i in range(1, size+1):
            if i not in frequency:
                res.append(i)
        if len(res) == 2:
            return res
        else:
            res.append(size+1)
            return res
