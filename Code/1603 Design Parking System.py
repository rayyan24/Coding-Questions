class ParkingSystem:

    def __init__(self, big: int, medium: int, small: int):
        self.big=big
        self.medium=medium
        self.small=small

    def addCar(self, carType: int) -> bool:
        '''
        big --> 1
        medium --> 2
        small --> 3
        '''
        res=None
        if carType==1:
            self.big-=1
            res=self.big>=0
        elif carType==2:
            self.medium-=1
            res=self.medium>=0
        else:
            self.small-=1
            res=self.small>=0
        return res

# Your ParkingSystem object will be instantiated and called as such:
# obj = ParkingSystem(big, medium, small)
# param_1 = obj.addCar(carType)