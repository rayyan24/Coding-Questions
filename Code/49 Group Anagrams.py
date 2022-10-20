import collections


class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        #         defaultdict returns the specified element insted of a key error
        ans = collections.defaultdict(list)
        for curSTR in strs:
            count = [0]*26
            for char in curSTR:
                count[ord(char)-ord("a")] += 1
            ans[tuple(count)].append(curSTR)
        return (ans.values())
