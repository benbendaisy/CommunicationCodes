import heapq
from typing import List


class Solution:
    """
        Suppose LeetCode will start its IPO soon. In order to sell a good price of its shares to Venture Capital, LeetCode would like to work on some projects to increase its capital before the IPO. Since it has limited resources, it can only finish at most k distinct projects before the IPO. Help LeetCode design the best way to maximize its total capital after finishing at most k distinct projects.

        You are given n projects where the ith project has a pure profit profits[i] and a minimum capital of capital[i] is needed to start it.

        Initially, you have w capital. When you finish a project, you will obtain its pure profit and the profit will be added to your total capital.

        Pick a list of at most k distinct projects from given projects to maximize your final capital, and return the final maximized capital.

        The answer is guaranteed to fit in a 32-bit signed integer.

        Example 1:

        Input: k = 2, w = 0, profits = [1,2,3], capital = [0,1,1]
        Output: 4
        Explanation: Since your initial capital is 0, you can only start the project indexed 0.
        After finishing it you will obtain profit 1 and your capital becomes 1.
        With capital 1, you can either start the project indexed 1 or the project indexed 2.
        Since you can choose at most 2 projects, you need to finish the project indexed 2 to get the maximum capital.
        Therefore, output the final maximized capital, which is 0 + 1 + 3 = 4.
        Example 2:

        Input: k = 3, w = 0, profits = [1,2,3], capital = [0,1,2]
        Output: 6
    """
    def findMaximizedCapital1(self, k: int, w: int, profits: List[int], capital: List[int]) -> int:
        n = len(profits)
        projects = list(zip(capital, profits))
        projects.sort()
        que = []
        ptr = 0
        for i in range(k):
            while ptr < n and projects[ptr][0] <= w:
                heapq.heappush(que, -projects[ptr][1])
                ptr += 1
            if not que:
                break
            w += -heapq.heappop(que)
        return w
    
    def findMaximizedCapital2(self, k: int, w: int, profits: List[int], capital: List[int]) -> int:
        """
        Time Limit Exceeded
        """
        def helper(choice: list, running_profit: int, steps: int) -> int:
            if steps == k or not choice:
                return running_profit

            max_profit = running_profit
            for i, v in enumerate(choice):
                if running_profit >= capital[v]:
                    max_profit = max(max_profit, helper(choice[:i] + choice[i + 1:], running_profit + profits[v], steps + 1))
            return max_profit
        n = len(profits)
        res = helper([i for i in range(n)], w, 0)
        return res if res != float('-inf') else 0
    
    def findMaximizedCapital3(self, k: int, w: int, profits: List[int], capital: List[int]) -> int:
        n = len(profits)
        projects = list(zip(capital, profits))
        projects.sort()

        heap = []
        ptr = 0
        for _ in range(k):
            while ptr < n and projects[ptr][0] <= w:
                heapq.heappush(heap, -projects[ptr][1])
                ptr += 1
            if not heap:
                break
            w += -heapq.heappop(heap)
        return w

