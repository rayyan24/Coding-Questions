class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        result = 0
        for i in digits:
            result = (10*result)+i
        result += 1
        digits = [int(i) for i in str(result)]
        return (digits)
