class Solution:
    def threeConsecutiveOdds(self, arr: List[int]) -> bool:
        fil = [0, 1, 2]

        for i in range(len(arr)-2):
            if arr[fil[0]]%2 != 0 and arr[fil[1]]%2 != 0 and arr[fil[2]]%2 != 0:
                return True
            fil[0] += 1
            fil[1] += 1
            fil[2] += 1
        
        return False
        