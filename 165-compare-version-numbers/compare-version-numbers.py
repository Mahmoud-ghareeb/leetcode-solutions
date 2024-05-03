class Solution:
    def compareVersion(self, version1: str, version2: str) -> int:
        version1 = version1.split('.')
        version2 = version2.split('.')

        m, n = len(version1), len(version2)

        if m > n:
            version2 = version2 + ['0'] * (m-n)
        elif m < n:
            version1 = version1 + ['0'] * (n-m)

        for i in range(max(m, n)):
            if int(version1[i]) > int(version2[i]):
                return 1
            elif int(version1[i]) < int(version2[i]):
                return -1

        return 0
