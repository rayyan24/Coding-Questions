class Solution:
    def longestConsecutive(self, arr: List[int]) -> int:
        Set = set(arr)
        longest = 0
        for CE in arr:
            #           if true it means it is a start of a new subsequence
            if (CE-1) not in Set:
                length = 0
                while (CE+length) in Set:
                    length += 1
                longest = max(length, longest)
        return longest
