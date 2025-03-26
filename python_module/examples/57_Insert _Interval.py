from typing import List


class Solution:
    """
        You are given an array of non-overlapping intervals intervals where intervals[i] = [starti, endi] represent the start and the end of the ith interval and intervals is sorted in ascending order by starti. You are also given an interval newInterval = [start, end] that represents the start and end of another interval.

        Insert newInterval into intervals such that intervals is still sorted in ascending order by starti and intervals still does not have any overlapping intervals (merge overlapping intervals if necessary).

        Return intervals after the insertion.

        Example 1:

        Input: intervals = [[1,3],[6,9]], newInterval = [2,5]
        Output: [[1,5],[6,9]]
        Example 2:

        Input: intervals = [[1,2],[3,5],[6,7],[8,10],[12,16]], newInterval = [4,8]
        Output: [[1,2],[3,10],[12,16]]
        Explanation: Because the new interval [4,8] overlaps with [3,5],[6,7],[8,10].
    """
    def insert1(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        res = []
        n = len(intervals)
        for i in range(n):
            if newInterval[1] < intervals[i][0]:
                res.append(newInterval)
                return res + intervals[i:]
            elif newInterval[0] > intervals[i][1]:
                res.append(intervals[i])
            else:
                newInterval = [min(newInterval[0], intervals[i][0]), max(newInterval[1], intervals[i][1])]
        res.append(newInterval)
        return res
    
    def insert2(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        res, is_added = [], False
        for start, end in intervals:
            if start <= newInterval[1] and newInterval[0] <= end:
                start = min(start, newInterval[0])
                end = max(end, newInterval[1])
                is_added = True
            if not res or res[-1][1] < start:
                res.append([start, end])
            elif start <= res[-1][1] and res[-1][0] <= end:
                res[-1][0] = min(res[-1][0], start)
                res[-1][1] = max(res[-1][1], end)
        if not is_added:
            res.append(newInterval)
            res.sort()
        return res
    
    def insert3(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        res = []
        i, n = 0, len(intervals)
        
        # Add all intervals before newInterval
        while i < n and intervals[i][1] < newInterval[0]:
            res.append(intervals[i])
            i += 1
        
        # Merge overlapping intervals
        while i < n and intervals[i][0] <= newInterval[1]:
            newInterval[0] = min(newInterval[0], intervals[i][0])
            newInterval[1] = max(newInterval[1], intervals[i][1])
            i += 1
        res.append(newInterval)
        
        # Add remaining intervals
        while i < n:
            res.append(intervals[i])
            i += 1
        
        return res
    
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        n = len(intervals)
        res, idx = [], 0
        while idx < n and intervals[idx][1] < newInterval[0]:
            res.append(intervals[idx])
            idx += 1

        while idx < n and intervals[idx][0] <= newInterval[1]:
            newInterval[0] = min(intervals[idx][0], newInterval[0])
            newInterval[1] = max(intervals[idx][1], newInterval[1])
            idx += 1
        res.append(newInterval)
        while idx < n:
            res.append(intervals[idx])
            idx += 1
        return res