class RandomizedSet:

    def __init__(self):
        self.items = dict()
        self.length = 0
        self.idxs = []
        

    def insert(self, val: int) -> bool:
        if val in self.items:
            return False
        self.items[val] = self.length
        self.idxs.append(val)
        self.length += 1
        return True        

    def remove(self, val: int) -> bool:
        if val not in self.items:
            return False

        idx = self.items[val]
        temp = self.idxs[-1]
        self.idxs[-1] = val
        self.idxs[idx] = temp
        self.items[temp] = idx

        self.items.pop(val, None)
        self.idxs.pop()
        self.length -= 1
        return True

    def getRandom(self) -> int:
        return random.choice(self.idxs)


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()