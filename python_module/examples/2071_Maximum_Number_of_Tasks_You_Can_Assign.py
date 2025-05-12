class Solution:
    """
    You have n tasks and m workers. Each task has a strength requirement stored in a 0-indexed integer array tasks, with the ith task requiring tasks[i] strength to complete. The strength of each worker is stored in a 0-indexed integer array workers, with the jth worker having workers[j] strength. Each worker can only be assigned to a single task and must have a strength greater than or equal to the task's strength requirement (i.e., workers[j] >= tasks[i]).

    Additionally, you have pills magical pills that will increase a worker's strength by strength. You can decide which workers receive the magical pills, however, you may only give each worker at most one magical pill.

    Given the 0-indexed integer arrays tasks and workers and the integers pills and strength, return the maximum number of tasks that can be completed.

    Example 1:

    Input: tasks = [3,2,1], workers = [0,3,3], pills = 1, strength = 1
    Output: 3
    Explanation:
    We can assign the magical pill and tasks as follows:
    - Give the magical pill to worker 0.
    - Assign worker 0 to task 2 (0 + 1 >= 1)
    - Assign worker 1 to task 1 (3 >= 2)
    - Assign worker 2 to task 0 (3 >= 3)
    Example 2:

    Input: tasks = [5,4], workers = [0,0,0], pills = 1, strength = 5
    Output: 1
    Explanation:
    We can assign the magical pill and tasks as follows:
    - Give the magical pill to worker 0.
    - Assign worker 0 to task 0 (0 + 5 >= 5)
    Example 3:

    Input: tasks = [10,15,30], workers = [0,10,10,10,10], pills = 3, strength = 10
    Output: 2
    Explanation:
    We can assign the magical pills and tasks as follows:
    - Give the magical pill to worker 0 and worker 1.
    - Assign worker 0 to task 0 (0 + 10 >= 10)
    - Assign worker 1 to task 1 (10 + 10 >= 15)
    The last pill is not given because it will not make any worker strong enough for the last task.
    """
    def maxTaskAssign1(self, tasks: List[int], workers: List[int], pills: int, strength: int) -> int:
        """
        Time Limit Exceed
        """
        tasks.sort()
        workers.sort()

        n, m = len(tasks), len(workers)

        @lru_cache(maxsize=None)
        def dfs(t_idx, w_mask, pills_left):
            if t_idx == n:
                return 0  # All tasks have been assigned
            
            max_done = 0
            for w_idx in range(m):
                if not (w_mask & (1 << w_idx)):  # Worker not yet used
                    worker_strength = workers[w_idx]
                    task_strength = tasks[t_idx]

                    # Option 1: assign without pill
                    if worker_strength >= task_strength:
                        max_done = max(max_done,
                                    1 + dfs(t_idx + 1, w_mask | (1 << w_idx), pills_left))
                    
                    # Option 2: assign with pill (if available)
                    elif pills_left > 0 and (worker_strength + strength) >= task_strength:
                        max_done = max(max_done,
                                    1 + dfs(t_idx + 1, w_mask | (1 << w_idx), pills_left - 1))
            return max_done

        return dfs(0, 0, pills)
    
    def maxTaskAssign2(self, tasks: List[int], workers: List[int], pills: int, strength: int) -> int:
        n, m = len(tasks), len(workers)
        tasks.sort()
        workers.sort()

        def check(mid: int) -> bool:
            p = pills
            # Ordered set of workers
            ws = SortedList(workers[m - mid :])
            # Enumerate each task from largest to smallest
            for i in range(mid - 1, -1, -1):
                # If the largest element in the ordered set is greater than or equal to tasks[i]
                if ws[-1] >= tasks[i]:
                    ws.pop()
                else:
                    if p == 0:
                        return False
                    rep = ws.bisect_left(tasks[i] - strength)
                    if rep == len(ws):
                        return False
                    p -= 1
                    ws.pop(rep)
            return True

        left, right, ans = 1, min(m, n), 0
        while left <= right:
            mid = (left + right) // 2
            if check(mid):
                ans = mid
                left = mid + 1
            else:
                right = mid - 1

        return ans
    
    def maxTaskAssign(self, tasks: List[int], workers: List[int], pills: int, strength: int) -> int:
        m, n = len(tasks), len(workers)
        tasks.sort()
        workers.sort()
        @cache
        def helper(t_idx: int, w_mask: int, pills_left: int) -> int:
            if t_idx == m:
                return 0
            
            max_tasks = 0
            for w_idx in range(n):
                if w_mask & (1 << w_idx) != 0:
                    continue
                new_mask = w_mask | (1 << w_idx)
                # option 1: can assign the task directly
                if workers[w_idx] >= tasks[t_idx]:
                    max_tasks = max(max_tasks, 1 + helper(t_idx + 1, new_mask, pills_left))
                # option2: can assign the task after taking the pills
                elif pills_left > 0 and (workers[w_idx] + strength) >= tasks[t_idx]:
                    max_tasks = max(max_tasks, 1 + helper(t_idx + 1, new_mask, pills_left - 1))
            return max_tasks
        return helper(0, 0, pills)