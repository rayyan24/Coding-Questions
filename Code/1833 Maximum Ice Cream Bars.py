class Solution:
    def maxIceCream(self, costs: List[int], totalCoins: int) -> int:
        costs.sort()
        res=0
        for cost in costs:
            if cost<=totalCoins:
                res+=1
                totalCoins-=cost
                continue
            break
        return res