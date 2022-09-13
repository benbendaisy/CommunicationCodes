from collections import deque


class Solution:
    """
        You are given two jugs with capacities jug1Capacity and jug2Capacity liters. There is an infinite amount of water supply available. Determine whether it is possible to measure exactly targetCapacity liters using these two jugs.

        If targetCapacity liters of water are measurable, you must have targetCapacity liters of water contained within one or both buckets by the end.

        Operations allowed:

        Fill any of the jugs with water.
        Empty any of the jugs.
        Pour water from one jug into another till the other jug is completely full, or the first jug itself is empty.

        Example 1:

        Input: jug1Capacity = 3, jug2Capacity = 5, targetCapacity = 4
        Output: true
        Explanation: The famous Die Hard example
        Example 2:

        Input: jug1Capacity = 2, jug2Capacity = 6, targetCapacity = 5
        Output: false
        Example 3:

        Input: jug1Capacity = 1, jug2Capacity = 2, targetCapacity = 3
        Output: true

        Constraints:

        1 <= jug1Capacity, jug2Capacity, targetCapacity <= 106
    """
    def canMeasureWater(self, jug1Capacity: int, jug2Capacity: int, targetCapacity: int) -> bool:
        queue = deque([(0, 0)])
        cache = {}


        while queue:
            jug1, jug2 = queue.popleft()
            if jug1 + jug2 == targetCapacity:
                return True

            states = [
                [jug1Capacity, jug2], #fill first one
                [jug1, jug2Capacity], #fill second one
                [max(0, jug1 - (jug2Capacity - jug2)), min(jug2Capacity, jug2 + jug1)], #pour first one into second one
                [min(jug1Capacity, jug2 + jug1), max(0, jug2 - (jug1Capacity - jug1))], #pour second one into first one
                [0, jug2],
                [jug1, 0]
            ]

            for dx, dy in states:
                if (dx, dy) not in cache:
                    queue.appendleft((dx, dy))
                    cache[(dx, dy)] = True

        return False