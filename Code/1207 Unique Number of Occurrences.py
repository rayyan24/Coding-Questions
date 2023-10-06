class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        freq=Counter(arr)
        Set=set()
        for i in freq.values():
            if  i in Set:
                return False
            else:
                Set.add(i)
        return True