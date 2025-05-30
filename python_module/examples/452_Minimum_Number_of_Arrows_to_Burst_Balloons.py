from typing import List


class Solution:
    """
        There are some spherical balloons taped onto a flat wall that represents the XY-plane. The balloons are represented as a 2D integer array points where points[i] = [xstart, xend] denotes a balloon whose horizontal diameter stretches between xstart and xend. You do not know the exact y-coordinates of the balloons.

        Arrows can be shot up directly vertically (in the positive y-direction) from different points along the x-axis. A balloon with xstart and xend is burst by an arrow shot at x if xstart <= x <= xend. There is no limit to the number of arrows that can be shot. A shot arrow keeps traveling up infinitely, bursting any balloons in its path.

        Given the array points, return the minimum number of arrows that must be shot to burst all balloons.

        Example 1:

        Input: points = [[10,16],[2,8],[1,6],[7,12]]
        Output: 2
        Explanation: The balloons can be burst by 2 arrows:
        - Shoot an arrow at x = 6, bursting the balloons [2,8] and [1,6].
        - Shoot an arrow at x = 11, bursting the balloons [10,16] and [7,12].
        Example 2:

        Input: points = [[1,2],[3,4],[5,6],[7,8]]
        Output: 4
        Explanation: One arrow needs to be shot for each balloon for a total of 4 arrows.
        Example 3:

        Input: points = [[1,2],[2,3],[3,4],[4,5]]
        Output: 2
        Explanation: The balloons can be burst by 2 arrows:
        - Shoot an arrow at x = 2, bursting the balloons [1,2] and [2,3].
        - Shoot an arrow at x = 4, bursting the balloons [3,4] and [4,5].
    """
    def findMinArrowShots1(self, points: List[List[int]]) -> int:
        if not points:
            return 0

        points.sort(key=lambda x: x[1])
        arrows_cnt = 1
        first_end = points[0][1]
        for start, end in points:
            if first_end < start:
                arrows_cnt += 1
                first_end = end
        return arrows_cnt
    
    def findMinArrowShots2(self, points: List[List[int]]) -> int:
        if not points:
            return 0
        points.sort(key=lambda x: (x[1], x[0]))
        end_point = points[0][1]
        arrow_cnt = 1
        for point in points:
            if end_point < point[0]:
                arrow_cnt += 1
                end_point = point[1]
        return arrow_cnt
    
    def findMinArrowShots3(self, points: List[List[int]]) -> int:
        if not points:
            return 0
        points.sort(key=lambda x: (x[1], x[0]))
        end_point = points[0][1]
        arr_cnt = 1
        for point in points:
            if end_point < point[0]:
                arr_cnt += 1
                end_point = point[1]
        return arr_cnt