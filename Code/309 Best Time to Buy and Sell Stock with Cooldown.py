class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        cache={}# key=(index,state) val= max profit
        # state --> True --> Buying
        # state --> False --> Selling
#       Every time we have three possible decisions buy sell cooldown(must)    
        def helper(index,buying):  
            if index>=len(prices):
                return 0
            if (index,buying) in cache:
                return cache[(index,buying)]
            cooldown=helper(index+1,buying)
            if buying==True:
                # -prices[i] because on current day we will have to spend money to buy the stock which reduces the profit
                buy=helper(index+1,not buying)-prices[index]
                cache[(index,buying)]=max(buy,cooldown)
            elif buying==False:
                # +prices[i] because on current day we will make some money which increases the profit
                sell=helper(index+2,not buying)+prices[index]
                cache[(index,buying)]=max(sell,cooldown)
            return cache[(index,buying)]
        return helper(0,True)