class Solution:
    def timeRequiredToBuy(self, tickets: List[int], k: int) -> int:

        q = deque()
        for i in range(len(tickets)):
            q.append(i)
            
        sol = 0
        while True:
            if tickets[k] == 0: break
            c = q.popleft()
            if tickets[c]>0:
               tickets[c] -= 1
               sol += 1
               q.append(c)
        
        return sol

        