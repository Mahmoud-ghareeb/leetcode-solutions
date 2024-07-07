class Solution:
    def numWaterBottles(self, numBottles: int, numExchange: int) -> int:
        sol = numBottles
        while True:
            sol += numBottles//numExchange
            numBottles = (numBottles//numExchange) + (numBottles%numExchange)
            if numBottles < numExchange:
                break

        return sol