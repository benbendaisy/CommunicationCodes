import heapq
from typing import List


class Solution:
    """
        There are n workers. You are given two integer arrays quality and wage where quality[i] is the quality of the ith worker and wage[i] is the minimum wage expectation for the ith worker.

        We want to hire exactly k workers to form a paid group. To hire a group of k workers, we must pay them according to the following rules:

        Every worker in the paid group should be paid in the ratio of their quality compared to other workers in the paid group.
        Every worker in the paid group must be paid at least their minimum wage expectation.
        Given the integer k, return the least amount of money needed to form a paid group satisfying the above conditions. Answers within 10-5 of the actual answer will be accepted.

        Example 1:

        Input: quality = [10,20,5], wage = [70,50,30], k = 2
        Output: 105.00000
        Explanation: We pay 70 to 0th worker and 35 to 2nd worker.

        Example 2:

        Input: quality = [3,1,10,10,1], wage = [4,8,2,2,7], k = 3
        Output: 30.66667
        Explanation: We pay 4 to 0th worker, 13.33333 to 2nd and 3rd workers separately.
    """
    def mincostToHireWorkers1(self, quality: List[int], wage: List[int], k: int) -> float:
        # --- Sort Workers by Ratio
        workers = [(w/q, q) for w, q in zip(wage, quality)]
        workers.sort()

        # --- Initialize Quality Max-Heap
        paid_group = [-1 * q for r, q in workers[:k]]
        heapq.heapify(paid_group)
        sum_q = -1 * sum(paid_group)

        # --- Initialize Cost with Captain = K
        cost = sum_q * workers[k - 1][0]

        # --- Test more expensive Captains.
        #       higher captain's ratio may be worth it if we can reduce sum_q
        for ratio, q in workers[k:]:
            sum_q += q + heapq.heappushpop(paid_group, -q)
            temp = ratio * sum_q
            cost = min(cost, temp)

        return cost

    def mincostToHireWorkers(self, quality: List[int], wage: List[int], k: int) -> float:
        workers = sorted([(w/q, q) for w, q in zip(wage, quality)])
        res = float('inf')
        qsum = 0
        heap = []
        for r, q in workers:
            heapq.heappush(heap, -q)
            qsum += q
            if len(heap) > k:
                qsum += heapq.heappop(heap)
            if len(heap) == k:
                res = min(res, qsum * r)
        return res