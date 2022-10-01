class Solution:
    def containsDuplicate(self, arr: List[int]) -> bool:
        hmap=set()
        for i in arr:
            if i in hmap:
                return True
            else:
                hmap.add(i)
        return False