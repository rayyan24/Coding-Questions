class Solution:
    def partition(self, s: str) -> List[List[str]]:
        res = []
        size = len(s)
        def helper( index, ds):
            if index == size:
                res.append(ds[:])
                return
            for i in range(index, size):
                # if prefix is pallindrome then only we will call recursive function again on rest of the string
                prefix = s[index:i+1]
                if prefix == prefix[::-1]:
                    helper(i+1, ds+[prefix])
        helper(0, [])
        return res