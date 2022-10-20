class Solution:
    def countOdds(self, low: int, high: int) -> int:
        # count odd numbers in a range
        # count(upperbound-lowerbound)//2
        # if upper bound or lower bound is odd do count+=1
        count = (high-low)//2
        if high % 2 != 0 or low % 2 != 0:
            count += 1
        return count
