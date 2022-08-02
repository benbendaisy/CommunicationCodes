from typing import List


class Solution:
    """
        You are given an array of integers distance.

        You start at point (0,0) on an X-Y plane and you move distance[0] meters to the north, then distance[1] meters to the west, distance[2] meters to the south, distance[3] meters to the east, and so on. In other words, after each move, your direction changes counter-clockwise.

        Return true if your path crosses itself, and false if it does not.

        Example 1:

        Input: distance = [2,1,1,2]
        Output: true
        Example 2:

        Input: distance = [1,2,3,4]
        Output: false
        Example 3:

        Input: distance = [1,1,1,1]
        Output: true

        Constraints:

        1 <= distance.length <= 105
        1 <= distance[i] <= 105
    """
    def isSelfCrossing(self, distance: List[int]) -> bool:
        for i in range(3,len(distance)):  # must have length to intersect
            if distance[i-3] >= distance[i-1] and distance[i] >= distance[i-2]:  # length of 3rd should be greater than 1st
                return True

            if i>=4:
                if distance[i-3] == distance[i-1] and distance[i-2] <= (distance[i-4] + distance[i]):
                    return True

            if i>=5:
                if distance[i-2] >= distance[i-4] and distance[i-3] >= distance[i-1] and (distance[i-5] + distance[i-1]) >= distance[i-3] and (distance[i-4] + distance[i]) >= distance[i-2]:
                    return True

        return False