List=list
class Solution:
    def twoSum(self, arr: List[int], target: int) -> List[int]:
        map = {}
        size = len(arr)
        for i in range(size):
            reqVal = target-arr[i]
            if (map.get(reqVal) != None):
                return [i, map[reqVal]]
            else:
                map[arr[i]] = i