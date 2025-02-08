from sortedcontainers import SortedList
import bisect

class NumberContainers:

    def __init__(self):
        self.cont = defaultdict(int)
        self.d = defaultdict(SortedList)

    def change(self, index: int, number: int) -> None:
        tmp = self.cont[index]
        self.cont[index] = number
        if tmp:
            self.d[tmp].remove(index)

        self.d[number].add(index)
        
    def find(self, number: int) -> int:
        if number in self.d and self.d[number]:
            return self.d[number][0]
        
        return -1
        


# Your NumberContainers object will be instantiated and called as such:
# obj = NumberContainers()
# obj.change(index,number)
# param_2 = obj.find(number)