class RandomizedSet:

    def __init__(self):
        self.Set=set()

    def insert(self, val: int) -> bool:
        if val not in self.Set:
            self.Set.add(val)
            return True
        else:
            self.Set.add(val)
            return False
    def remove(self, val: int) -> bool:
        if val in self.Set:
            self.Set.remove(val)
            return True
        else:
            return False
    def getRandom(self) -> int:
        List=list(self.Set)
        return random.choice(List)

# sets are non-subsciptable
# sets can be typecated to lists