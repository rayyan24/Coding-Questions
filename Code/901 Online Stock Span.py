class StockSpanner:

    def __init__(self):
        self.priceStack=[]
        self.spanStack=[]
                
    def next(self, price: int) -> int:
        span=1
        while self.priceStack and self.priceStack[-1]<=price:
            span+=self.spanStack[-1]
            self.priceStack.pop()
            self.spanStack.pop()
        self.priceStack.append(price)
        self.spanStack.append(span)
        return span