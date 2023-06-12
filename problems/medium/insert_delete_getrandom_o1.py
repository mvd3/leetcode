class RandomizedSet:

    def __init__(self):
        self.d = [] # data
        self.m = {} # map of the data

    def insert(self, val: int) -> bool:
        if val in self.m:
            return False
        self.m[val] = len(self.d)
        self.d.append(val)
        return True

    def remove(self, val: int) -> bool:
        if val not in self.m:
            return False
        
        le = self.d[-1] # last element
        rei = self.m[val] # index of element to be removed
        self.m[le] = rei
        self.d[rei] = le
        del self.m[val], self.d[-1]

        return True

    def getRandom(self) -> int:
        return random.choice(self.d)