class Solution:
    def divideString(self, s: str, k: int, fill: str) -> List[str]:
        n = len(s)
        r = n % k
        sol = [s[i:i+k] for i in range(0, len(s), k)]
        if r:
            sol[-1] = sol[-1] + (k-r)*fill

        return sol
        
        