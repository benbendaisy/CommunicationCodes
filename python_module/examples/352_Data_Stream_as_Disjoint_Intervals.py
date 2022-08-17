from typing import List


class SummaryRanges:

    def __init__(self):
        self.parents = {}
        self.intervals = {}

    def find(self, x):
        if x not in self.parents:
            return None
        if x != self.parents[x]:
            x = self.find(self.parents[x])
        return self.parents[x]

    def union(self, x, y):
        # x < y
        px, py = self.find(x), self.find(y)
        if px == None or py == None:
            return
        self.parents[py] = px
        self.intervals[px] = max(self.intervals[px], self.intervals[py])
        del self.intervals[py]

    def addNum(self, val: int) -> None:
        if val in self.parents:
            return
        self.parents[val] = val
        self.intervals[val] = val
        self.union(val-1, val)
        self.union(val, val+1)

    def getIntervals(self) -> List[List[int]]:
        res = []
        intervals_start = sorted(self.intervals.keys())
        for s in intervals_start:
            res.append([s, self.intervals[s]])
        return res


class SummaryRanges1:
    """
        Given a data stream input of non-negative integers a1, a2, ..., an, summarize the numbers seen so far as a list of disjoint intervals.

        Implement the SummaryRanges class:

        SummaryRanges() Initializes the object with an empty stream.
        void addNum(int val) Adds the integer val to the stream.
        int[][] getIntervals() Returns a summary of the integers in the stream currently as a list of disjoint intervals [starti, endi].

        Example 1:

        Input
        ["SummaryRanges", "addNum", "getIntervals", "addNum", "getIntervals", "addNum", "getIntervals", "addNum", "getIntervals", "addNum", "getIntervals"]
        [[], [1], [], [3], [], [7], [], [2], [], [6], []]
        Output
        [null, null, [[1, 1]], null, [[1, 1], [3, 3]], null, [[1, 1], [3, 3], [7, 7]], null, [[1, 3], [7, 7]], null, [[1, 3], [6, 7]]]

        Explanation
        SummaryRanges summaryRanges = new SummaryRanges();
        summaryRanges.addNum(1);      // arr = [1]
        summaryRanges.getIntervals(); // return [[1, 1]]
        summaryRanges.addNum(3);      // arr = [1, 3]
        summaryRanges.getIntervals(); // return [[1, 1], [3, 3]]
        summaryRanges.addNum(7);      // arr = [1, 3, 7]
        summaryRanges.getIntervals(); // return [[1, 1], [3, 3], [7, 7]]
        summaryRanges.addNum(2);      // arr = [1, 2, 3, 7]
        summaryRanges.getIntervals(); // return [[1, 3], [7, 7]]
        summaryRanges.addNum(6);      // arr = [1, 2, 3, 6, 7]
        summaryRanges.getIntervals(); // return [[1, 3], [6, 7]]

        Constraints:

        0 <= val <= 104
        At most 3 * 104 calls will be made to addNum and getIntervals.
    """

    def __init__(self):
        self.intervals = []


    def addNum(self, val: int) -> None:
        left, right = 0, len(self.intervals) - 1
        while left <= right:
            mid = (left + right) // 2
            e = self.intervals[mid]
            if e[0] <= val <= e[1]:
                return
            elif val < e[0]:
                right = mid - 1
            else:
                left = mid + 1

        pos = left
        self.intervals.insert(pos, [val, val])
        if pos + 1 < len(self.intervals) and val + 1 == self.intervals[pos + 1][0]:
            self.intervals[pos][1] = self.intervals[pos + 1][1]
            del self.intervals[pos + 1]

        if pos - 1 >= 0 and val - 1 == self.intervals[pos - 1][1]:
            self.intervals[pos - 1][1] = self.intervals[pos][1]
            del self.intervals[pos]

    def getIntervals(self) -> List[List[int]]:
        return self.intervals