from collections import defaultdict
from typing import List


class Solution:
    """
    Given n points on a 2D plane, find if there is such a line parallel to the y-axis that reflects the given points symmetrically.

    In other words, answer whether or not if there exists a line that after reflecting all points over the given line, the original points' set is the same as the reflected ones.

    Note that there can be repeated points.

    Example 1:

    Input: points = [[1,1],[-1,1]]
    Output: true
    Explanation: We can choose the line x = 0.
    Example 2:

    Input: points = [[1,1],[-1,-1]]
    Output: false
    Explanation: We can't choose a line.

    Constraints:

    n == points.length
    1 <= n <= 104
    -108 <= points[i][j] <= 108
    """
    def isReflected(self, points: List[List[int]]) -> bool:
        hdict = defaultdict(set)
        for x, y in points:
            hdict[y].add(x)

        meds = set()
        for y, xs in hdict.items():
            med = sum(xs) / len(xs)
            if sum([x - med for x in xs]) != 0:
                return False
            meds.add(med)

        return len(meds) == 1

if __name__ == "__main__":
    points = [[1,1],[0,0],[-1,1]]
    solution = Solution()
    ret = solution.isReflected(points)
    print(ret)
