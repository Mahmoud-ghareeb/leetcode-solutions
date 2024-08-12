class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.k = k
        self.hq = nums
        heapq.heapify(self.hq)

        print(self.hq)

        while len(self.hq) > k:
            heapq.heappop(self.hq)


    def add(self, val: int) -> int:
        heapq.heappush(self.hq, val)
        if len(self.hq) > self.k:
            heapq.heappop(self.hq)

        return self.hq[0]
        


# Your KthLargest object will be instantiated and called as such:
# obj = KthLargest(k, nums)
# param_1 = obj.add(val)