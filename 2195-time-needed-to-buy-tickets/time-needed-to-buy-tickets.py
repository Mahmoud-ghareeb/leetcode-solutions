class Solution:
    def timeRequiredToBuy(self, tickets: List[int], k: int) -> int:

        sol = 0
        for idx, num in enumerate(tickets):
            if idx>k:
                sol += min(tickets[k]-1, num)
            else:
                sol += min(tickets[k], num)

        return sol

        