class Solution:
    def mostFrequentEven(self, nums: List[int]) -> int:
        Map=Counter([i for i in nums if i%2==0])
        #a=type(list(Map.items())[0]) #tuple
        item1,item2=-1,-1
        freq=-1
        # res = {x: count for x, count in counter.items() if count == max(counter.values())}
        if not Map:
            return -1
        ans={}
        MAX=max(Map.values())
        for value,count in Map.items():
            if count==MAX:
                ans[value]=count
        return min(ans.keys())
            