from typing import List


class Solution:
    """
    You are given an array of events where events[i] = [startDayi, endDayi, valuei]. The ith event starts at startDayi and ends at endDayi, and if you attend this event, you will receive a value of valuei. You are also given an integer k which represents the maximum number of events you can attend.

    You can only attend one event at a time. If you choose to attend an event, you must attend the entire event. Note that the end day is inclusive: that is, you cannot attend two events where one of them starts and the other ends on the same day.

    Return the maximum sum of values that you can receive by attending events.

    Example 1:

    Input: events = [[1,2,4],[3,4,3],[2,3,1]], k = 2
    Output: 7
    Explanation: Choose the green events, 0 and 1 (0-indexed) for a total value of 4 + 3 = 7.
    Example 2:

    Input: events = [[1,2,4],[3,4,3],[2,3,10]], k = 2
    Output: 10
    Explanation: Choose event 2 for a total value of 10.
    Notice that you cannot attend any other event as they overlap, and that you do not have to attend k events.
    Example 3:

    Input: events = [[1,1,1],[2,2,2],[3,3,3],[4,4,4]], k = 3
    Output: 9
    Explanation: Although the events do not overlap, you can only attend 3 events. Pick the highest valued three.
    """
    def maxValue1(self, events: List[List[int]], k: int) -> int:
        n = len(events)
        events.sort()
        @lru_cache(None)
        def dp(i, k):
            if not k or i >= n:
                return 0
            j = bisect.bisect_right(events, [events[i][1], inf, inf])
            return max(dp(i + 1, k), events[i][2] + dp(j, k - 1))
        return dp(0, k)
    
    def maxValue2(self, events: List[List[int]], k: int) -> int:
        n = len(events)
        dp = [[0 for _ in range(k + 1)] for _ in range(n + 1)]
        events.sort()
        starts = [x for x, y, z in events]

        for i in range(n - 1, -1, -1):
            for j in range(1, k + 1):
                next = bisect.bisect_right(starts, events[i][1])
                dp[i][j] = max(dp[i + 1][j], events[i][2] + dp[next][j - 1])
        return dp[0][k]
    
    def maxValue(self, events: List[List[int]], k: int) -> int:
        if not events:
            return 0
        
        events.sort()
        # Extract start days for binary search
        start_days = [x for x, _, _ in events]
        n = len(events)
        
        @cache
        def helper(idx: int, e: int):
            # Base case: No events or no choices left
            if idx == n or e == 0:
                return 0
            
            # Find the next available event that starts after events[i] ends
            next_id = bisect.bisect_right(start_days, events[idx][1])

            # Two choices: skip event[i] or attend it and jump to next non-overlapping event
            return max(
                helper(idx + 1, e), # Skip this event
                events[idx][2] + helper(next_id, e - 1) # Attend this event
            )
        
        # Start from first event with k selections available
        return helper(0, k)