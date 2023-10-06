class Solution:
    def shuffle(self, arr: List[int], n: int) -> List[int]:
        res=[]
        for i in range(n):
            res.extend([arr[i],arr[i+n]])
        return res