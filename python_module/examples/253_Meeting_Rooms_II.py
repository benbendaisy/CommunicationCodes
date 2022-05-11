import heapq
from collections import defaultdict
from typing import List


class Solution:
    def minMeetingRooms1(self, intervals: List[List[int]]) -> int:
        rooms = defaultdict(lambda: [])
        cnt = 1
        intervals.sort(key=lambda x: x[0])
        rooms[cnt].append(intervals[0])
        for interval in intervals[1:]:
            needExtraRoom = True
            for key, value in rooms.items():
                if value[-1][1] <= interval[0]:
                    needExtraRoom = False
                    value.append(interval)
                    break

            if needExtraRoom:
                cnt += 1
                rooms[cnt].append(interval)
        return cnt

    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        if not intervals:
            return 0

        rooms = []
        intervals.sort(key=lambda x: x[0])
        heapq.heappush(rooms, intervals[0][1])

        for interval in intervals[1:]:
            if rooms[0] <= interval[0]:
                heapq.heappop(rooms)

            heapq.heappush(rooms, interval[1])

        return len(rooms)

