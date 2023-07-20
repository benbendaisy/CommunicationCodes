from typing import List


class Solution:
    """
    You are given an array coordinates, coordinates[i] = [x, y], where [x, y] represents the coordinate of a point. Check if these points make a straight line in the XY plane.

    Example 1:

    Input: coordinates = [[1,2],[2,3],[3,4],[4,5],[5,6],[6,7]]
    Output: true
    Example 2:

    Input: coordinates = [[1,1],[2,2],[3,4],[4,5],[5,6],[7,7]]
    Output: false
    """
    def checkStraightLine(self, coordinates: List[List[int]]) -> bool:
        n = len(coordinates)
        x1, y1 = coordinates[0]
        x2, y2 = coordinates[1]
        for i in range(2, n):
            x, y = coordinates[i]
            if (y - y1) * (x - x2) != (y - y2) * (x - x1):
                return False
        return True