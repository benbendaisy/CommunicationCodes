from typing import List


class Solution:
    """
    Given an array of intervals where intervals[i] = [starti, endi], merge all overlapping intervals, and return an array of the non-overlapping intervals that cover all the intervals in the input.

    Example 1:

    Input: intervals = [[1,3],[2,6],[8,10],[15,18]]
    Output: [[1,6],[8,10],[15,18]]
    Explanation: Since intervals [1,3] and [2,6] overlap, merge them into [1,6].
    Example 2:

    Input: intervals = [[1,4],[4,5]]
    Output: [[1,5]]
    Explanation: Intervals [1,4] and [4,5] are considered overlapping.
    """
    def merge1(self, intervals: List[List[int]]) -> List[List[int]]:
        # intervals = sorted(intervals)
        intervals.sort(key=lambda x: x[0])
        res = [intervals[0]]
        for start, end in intervals[1:]:
            last_end = res[-1][1]
            if last_end >= start:
                res[-1][1] = max(last_end, end)
            else:
                res.append([start, end])
        return res

    def merge2(self, intervals: List[List[int]]) -> List[List[int]]:
        if not intervals:
            return []
        intervals.sort()
        res = []
        for start, end in intervals:
            if not res or res[-1][1] < start:
                res.append([start, end])
            else:
                res[-1][1] = max(res[-1][1], end)
        return res