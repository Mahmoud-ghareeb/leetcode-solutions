class MyCalendar:

    def __init__(self):
        self.start = []
        self.end = []    

    def book(self, start: int, end: int) -> bool:
        for i in range(len(self.start)):
            if start >= self.start[i]:
                tmp = [self.start[i], self.end[i], start, end]
            else:
                tmp = [start, end, self.start[i], self.end[i]]
            s_tmp = sorted(tmp)
            are_equal = all(a == b for a, b in zip(tmp, s_tmp))
            if not are_equal:
                return False

            # if (self.end[i] > start >= self.start[i]) or (self.end[i] > end > self.start[i]):
            #     return False
        self.start.append(start)
        self.end.append(end)

        return True

        


# Your MyCalendar object will be instantiated and called as such:
# obj = MyCalendar()
# param_1 = obj.book(start,end)