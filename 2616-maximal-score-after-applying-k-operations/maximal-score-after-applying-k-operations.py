class Solution:
    def maxKelements(self, nums: List[int], k: int) -> int:
        
        heap = [-1 * num for num in nums]
        heapq.heapify(heap)
        
        sol = 0

        for i in range(k):
            num = heapq.heappop(heap) * -1
            sol += (num)
            heapq.heappush(heap, -1 * math.ceil(num/3))

        return sol       