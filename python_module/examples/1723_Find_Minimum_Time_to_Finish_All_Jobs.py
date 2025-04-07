class Solution:
    """
    You are given an integer array jobs, where jobs[i] is the amount of time it takes to complete the ith job.

    There are k workers that you can assign jobs to. Each job should be assigned to exactly one worker. The working time of a worker is the sum of the time it takes to complete all jobs assigned to them. Your goal is to devise an optimal assignment such that the maximum working time of any worker is minimized.

    Return the minimum possible maximum working time of any assignment.

    Example 1:

    Input: jobs = [3,2,3], k = 3
    Output: 3
    Explanation: By assigning each person one job, the maximum time is 3.
    Example 2:

    Input: jobs = [1,2,4,7,8], k = 2
    Output: 11
    Explanation: Assign the jobs the following way:
    Worker 1: 1, 2, 8 (working time = 1 + 2 + 8 = 11)
    Worker 2: 4, 7 (working time = 4 + 7 = 11)
    The maximum working time is 11.
    """
    def minimumTimeRequired1(self, jobs: List[int], k: int) -> int:
        """
        Memory Limit Exceeded
        """
        n = len(jobs)
        @cache
        def helper(idx: int, arr: tuple) -> int:
            if idx == n:
                return max(arr)
            arr = list(arr)
            min_max_time = float('inf')
            for j in range(k):
                arr[j] += jobs[idx]
                min_max_time = min(min_max_time, helper(idx + 1, tuple(arr)))
                arr[j] -= jobs[idx]
            return min_max_time
        return helper(0, tuple([0] * k))
    
    def minimumTimeRequired2(self, jobs: List[int], k: int) -> int:
        n = len(jobs)
        jobs.sort()
        self.min_max_time = float('inf')
        arr = [0] * k
        def helper(idx: int) -> int:
            if idx == n:
                self.min_max_time = min(self.min_max_time, max(arr))
                return
            max_time = max(arr)
            min_max_time = float('inf')
            for j in range(k):
                if arr[j] + jobs[idx] > self.min_max_time:
                    continue
                arr[j] += jobs[idx]
                helper(idx + 1)
                arr[j] -= jobs[idx]
                if arr[j] == 0:
                    break

        helper(0)
        return self.min_max_time