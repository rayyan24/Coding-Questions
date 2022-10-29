class Solution:
    def containsNearbyDuplicate(self, arr: List[int], k: int) -> bool:
        MAP={}
        for ind,val in enumerate(arr):
            if val in MAP and abs(ind-MAP.get(val))<=k:
                return True
            else:
                MAP[val]=ind
        return False