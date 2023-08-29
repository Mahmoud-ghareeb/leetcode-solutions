class Solution:
    def bestClosingTime(self, customers: str) -> int:

        n = len(customers)
        customers = list(customers)
        for i in range(n):
            if customers[i] == 'Y':
               customers[i] = 1
            else:
                customers[i] = 0
        
        def post_sum():
            d, s, p_y, p_n = [], 0, sum(customers), 0
            for i in range(n):
                d.append([p_y - s + p_n, i])
                s += customers[i]
                p_n += not(customers[i])
            d.append([p_y - s + p_n, n])

            return d

        d = sorted(post_sum())

        return d[0][1]