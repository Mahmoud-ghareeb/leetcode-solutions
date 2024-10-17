class Solution:
    def maximumSwap(self, num: int) -> int:

        max_queue = []
        min_queue = []
        s_num = [n for n in str(num)]

        heapq.heapify(max_queue)
        # heapq.heapify(min_queue)

        for idx,i in enumerate(s_num):
            heapq.heappush(max_queue, (-1*int(i), -1*idx))
            # heapq.heappush(min_queue, (int(i), idx))

        max_max = tuple([0, 1])
        for idx,i in enumerate(s_num):
            max_n = heapq.heappop(max_queue)
            # print(max_n)
            if (max_max[0]*-1) == (max_n[0] * -1) and (max_max[1]*-1) > (max_n[1] * -1):
                max_max = max_max
            # elif (max_max[0]*-1) == (max_n[0] * -1) and :
            else:
                max_max = max_n

            # print(max_max)
            if int(i) < (max_max[0] * -1):
                
                min_n =(int(i), idx)
                s_num[-1*max_max[1]] = str(min_n[0])
                s_num[min_n[1]] = str(max_max[0] * -1)
                return int(''.join(s_num))

    

        return num