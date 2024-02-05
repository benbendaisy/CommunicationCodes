from typing import List


class Solution:
    """
        Given an array of integers temperatures represents the daily temperatures, return an array answer such that answer[i] is the number of days you have to wait after the ith day to get a warmer temperature. If there is no future day for which this is possible, keep answer[i] == 0 instead.

        Example 1:

        Input: temperatures = [73,74,75,71,69,72,76,73]
        Output: [1,1,4,2,1,1,0,0]
        Example 2:

        Input: temperatures = [30,40,50,60]
        Output: [1,1,1,0]
        Example 3:

        Input: temperatures = [30,60,90]
        Output: [1,1,0]
    """
    def dailyTemperatures1(self, temperatures: List[int]) -> List[int]:
        if not temperatures:
            return 0
        n = len(temperatures)
        res = []
        for i in range(n):
            cnt = 1
            idx = i + 1
            while idx < n:
                if temperatures[i] >= temperatures[idx]:
                    cnt += 1
                else:
                    res.append(cnt)
                    break
                idx += 1
            if idx == n:
                res.append(0)
        return res

    def dailyTemperatures2(self, temperatures: List[int]) -> List[int]:
        if not temperatures:
            return []
        n = len(temperatures)
        res = [0] * n
        for day in range(n):
            for future_day in range(day + 1, n):
                if temperatures[future_day] > temperatures[day]:
                    res[day] = future_day - day
                    break
        return res

    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        if not temperatures:
            return []
        n = len(temperatures)
        res = [0] * n
        stack = []
        for cur_day, cur_temp in enumerate(temperatures):
            while stack and temperatures[stack[-1]] < cur_temp:
                prev_day = stack.pop()
                res[prev_day] = cur_day - prev_day
            stack.append(cur_day)
        return res

