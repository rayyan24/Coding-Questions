
class Solution:
    def __init__(self) -> None:
        self.max_len = 0

    def dfs(self, arr, curr_subseq, idx) -> None:
        # return if duplicate characters
        if len(curr_subseq) != len(set(curr_subseq)):
            return

        # update max_len if  curr_subseq is maximal
        self.max_len = max(len(curr_subseq), self.max_len)

        # dfs on next subseq(s) starting from curr_subseq
        for i in range(idx, len(arr)):
            self.dfs(arr, curr_subseq+arr[i], i+1)

    def maxLength(self, arr: List[str]) -> int:
        if not arr:
            return 0

        self.dfs(arr, "", 0)

        return self.max_len


class Solution:
    def maxLength(self, arr: List[str]) -> int:
        if not arr:
            return 0

        def helper(curStr, index)-> None:
            # Python 3 has introduced the nonlocal statement, which works much like the global statement, but lets us access variables of the surrounding function (rather than global variables).
            nonlocal maxLen
            curStrSize = len(curStr)
            # if true means current subsequence contains duplicate
            if curStrSize != len(set(curStr)):
                return 0
            # update max_len if  len cur string is greater than the previous Max
            maxLen = max(curStrSize, maxLen)
            for i in range(index, size):
                helper(curStr+arr[i], i+1)
        maxLen = 0
        size = len(arr)
        helper('', 0)
        return maxLen
