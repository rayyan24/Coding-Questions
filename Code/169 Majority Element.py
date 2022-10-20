class Solution:
    from collections import defaultdict

    def majorityElement(self, arr: List[int]) -> int:
        # size=len(arr)
        # count=defaultdict(set)
        # for i in arr:
        #     if i in count:
        #         count[i]+=1
        #     else:
        #         count[i]=1
        # count=dict(count)
        # print(count)
        # for key,value in zip(count.keys(),count.values()):
        #     if value>size//2:
        #         return key
        ans, count = 0, 0
        for i in arr:
            if count == 0:
                ans = i
            if i == ans:
                count += 1
            else:
                count -= 1
        return ans
