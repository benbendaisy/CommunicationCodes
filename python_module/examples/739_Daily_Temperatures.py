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
        for i in range(n):
            for j in range(i + 1, n):
                if temperatures[j] > temperatures[i]:
                    res[i] = j - i
                    break
        return res

    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        if not temperatures:
            return []
        n = len(temperatures)
        stack = []
        res = [0] * n
        for i, v in enumerate(temperatures):
            while stack and temperatures[stack[-1]] < v:
                prev = stack.pop()
                res[prev] = i - prev
            stack.append(i)
        return res



