from collections import defaultdict
from typing import List


class Solution:
    """
        You are given n points in the plane that are all distinct, where points[i] = [xi, yi]. A boomerang is a tuple of points (i, j, k) such that the distance between i and j equals the distance between i and k (the order of the tuple matters).

        Return the number of boomerangs.

        Example 1:

        Input: points = [[0,0],[1,0],[2,0]]
        Output: 2
        Explanation: The two boomerangs are [[1,0],[0,0],[2,0]] and [[1,0],[2,0],[0,0]].
        Example 2:

        Input: points = [[1,1],[2,2],[3,3]]
        Output: 2
        Example 3:

        Input: points = [[1,1]]
        Output: 0
    """
    def numberOfBoomerangs(self, points: List[List[int]]) -> int:
        boomerangs = 0
        for p1 in points:
            distances = defaultdict(int)
            for p2 in points:
                if p1 == p2:
                    continue
                dist = (p1[0] - p2[0]) ** 2 + (p1[1] - p2[1]) ** 2
                distances[dist] += 1
            for dist in distances.values():
                boomerangs += dist * (dist - 1)
        return boomerangs
