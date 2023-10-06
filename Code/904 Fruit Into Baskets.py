class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        left=0
        total=0
        res=0
        Map=collections.defaultdict(int)
        for right,value in enumerate(fruits):
            Map[value]+=1
            total+=1
            while len(Map)>2:
                leftVal=fruits[left]
                Map[leftVal]-=1
                total-=1
                left+=1
                if Map[leftVal]<1:
                    Map.pop(leftVal)
            res=max(res,total)
        return res