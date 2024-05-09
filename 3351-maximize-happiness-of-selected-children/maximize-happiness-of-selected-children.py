class Solution:
    def maximumHappinessSum(self, happiness: List[int], k: int) -> int:
        happiness.sort(reverse=True)

        sol, dec = 0, 0
        for i in range(k):
            sol += max(0, happiness[i] - dec)
            dec += 1

        return sol


        