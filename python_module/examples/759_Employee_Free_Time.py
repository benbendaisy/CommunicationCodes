
"""
# Definition for an Interval.
"""

class Interval:
    def __init__(self, start: int = None, end: int = None):
        self.start = start
        self.end = end

class Solution:
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