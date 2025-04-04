
"""
# Definition for an Interval.
"""

class Interval:
    def __init__(self, start: int = None, end: int = None):
        self.start = start
        self.end = end

class Solution:
    """
    We are given a list schedule of employees, which represents the working time for each employee.

    Each employee has a list of non-overlapping Intervals, and these intervals are in sorted order.

    Return the list of finite intervals representing common, positive-length free time for all employees, also in sorted order.

    (Even though we are representing Intervals in the form [x, y], the objects inside are Intervals, not lists or arrays. For example, schedule[0][0].start = 1, schedule[0][0].end = 2, and schedule[0][0][0] is not defined).  Also, we wouldn't include intervals like [5, 5] in our answer, as they have zero length.

    Example 1:

    Input: schedule = [[[1,2],[5,6]],[[1,3]],[[4,10]]]
    Output: [[3,4]]
    Explanation: There are a total of three employees, and all common
    free time intervals would be [-inf, 1], [3, 4], [10, inf].
    We discard any intervals that contain inf as they aren't finite.
    Example 2:

    Input: schedule = [[[1,3],[6,7]],[[2,4]],[[2,5],[9,12]]]
    Output: [[5,6],[7,9]]
    """
    def employeeFreeTime(self, schedule: '[[Interval]]') -> '[Interval]':
        events = []
        for employee in schedule:
            for event in employee:
                events.append(event)
        events.sort(key=operator.attrgetter('start'))

        res = []
        iterator = iter(events)
        prev_end = next(iterator).end
        for event in iterator:
            if event.start > prev_end:
                res.append(Interval(prev_end, event.start))
            prev_end = max(prev_end, event.end)
        return res
    
    def employeeFreeTime2(self, schedule: '[[Interval]]') -> '[Interval]':
        # Flatten and sort all intervals
        intervals = sorted([interval for employee in schedule for interval in employee], key=lambda x: x.start)
        
        merged = []
        for interval in intervals:
            if not merged or merged[-1].end < interval.start:
                merged.append(interval)
            else:
                merged[-1].end = max(merged[-1].end, interval.end)
        
        free_times = []
        for i in range(1, len(merged)):
            free_times.append(Interval(merged[i-1].end, merged[i].start))
        
        return free_times
    
    def employeeFreeTime(self, schedule: '[[Interval]]') -> '[Interval]':
        # Flatten and sort all intervals
        intervals = sorted([interval for employee in schedule for interval in employee], key=lambda x: x.start)

        merged = []
        for interval in intervals:
            if not merged or merged[-1].end < interval.start:
                merged.append(interval)
            else:
                merged[-1].end = max(merged[-1].end, interval.end)
        res = []
        for i in range(1, len(merged)):
            res.append(Interval(merged[i - 1].end, merged[i].start))
        return res
