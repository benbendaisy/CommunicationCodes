import math
from functools import lru_cache
from typing import List


class Solution:
    """
        You want to schedule a list of jobs in d days. Jobs are dependent (i.e To work on the ith job, you have to finish all the jobs j where 0 <= j < i).

        You have to finish at least one task every day. The difficulty of a job schedule is the sum of difficulties of each day of the d days. The difficulty of a day is the maximum difficulty of a job done on that day.

        You are given an integer array jobDifficulty and an integer d. The difficulty of the ith job is jobDifficulty[i].

        Return the minimum difficulty of a job schedule. If you cannot find a schedule for the jobs return -1.

        Example 1:

        Input: jobDifficulty = [6,5,4,3,2,1], d = 2
        Output: 7
        Explanation: First day you can finish the first 5 jobs, total difficulty = 6.
        Second day you can finish the last job, total difficulty = 1.
        The difficulty of the schedule = 6 + 1 = 7
        Example 2:

        Input: jobDifficulty = [9,9,9], d = 4
        Output: -1
        Explanation: If you finish a job per day you will still have a free day. you cannot find a schedule for the given jobs.
        Example 3:

        Input: jobDifficulty = [1,1,1], d = 3
        Output: 3
        Explanation: The schedule is one job per day. total difficulty will be 3.
    """
    def minDifficulty1(self, jobDifficulty: List[int], d: int) -> int:
        n = len(jobDifficulty)
        # Edge case: make sure there is at least one job per day
        if n < d:
            return -1

        # Precompute the maximum job difficulty for remaining jobs
        maxJobRemaining = jobDifficulty.copy()
        for i in range(n - 2, -1, -1):
            maxJobRemaining[i] = max(maxJobRemaining[i], maxJobRemaining[i + 1])

        # Use memoization to avoid repeated computation of min_diff states
        @lru_cache(None)
        def minDiff(idx, daysRemaining):
            # Base case: finish all remaining jobs in the last day
            if daysRemaining == 1:
                return maxJobRemaining[idx]

            res = math.inf
            dailyMaxJobDiff = 0 # keep track of the maximum difficulty for today

            # Iterate through possible starting index for the next day
            # and ensure we have at least one job for each remaining day.
            for j in range(idx, n - daysRemaining + 1):
                dailyMaxJobDiff = max(dailyMaxJobDiff, jobDifficulty[j])
                res = min(res, dailyMaxJobDiff + minDiff(j + 1, daysRemaining - 1))
            return res
        return minDiff(0, d)

    def minDifficulty(self, jobDifficulty: List[int], d: int) -> int:
        n = len(jobDifficulty)
        minDiff = [[float('inf')] * n + [0] for _ in range(d + 1)]
        for daysRemaining in range(1, d + 1):
            for i in range(n - daysRemaining + 1):
                dailyMaxJobDiff = 0
                for j in range(i + 1, n - daysRemaining + 2):
                    dailyMaxJobDiff = max(dailyMaxJobDiff, jobDifficulty[j - 1])
                    minDiff[daysRemaining][i] = min(minDiff[daysRemaining][i], dailyMaxJobDiff + minDiff[daysRemaining - 1][j])
        if minDiff[d][0] == float('inf'):
            return -1
        return minDiff[d][0]
