import bisect
from typing import List


class Solution:
    """
        Winter is coming! During the contest, your first job is to design a standard heater with a fixed warm radius to warm all the houses.

        Every house can be warmed, as long as the house is within the heater's warm radius range.

        Given the positions of houses and heaters on a horizontal line, return the minimum radius standard of heaters so that those heaters could cover all houses.

        Notice that all the heaters follow your radius standard, and the warm radius will the same.

        Example 1:

        Input: houses = [1,2,3], heaters = [2]
        Output: 1
        Explanation: The only heater was placed in the position 2, and if we use the radius 1 standard, then all the houses can be warmed.
        Example 2:

        Input: houses = [1,2,3,4], heaters = [1,4]
        Output: 1
        Explanation: The two heater was placed in the position 1 and 4. We need to use radius 1 standard, then all the houses can be warmed.
        Example 3:

        Input: houses = [1,5], heaters = [2]
        Output: 3
    """
    def findRadius1(self, houses: List[int], heaters: List[int]) -> int:
        houses.sort()
        heaters.sort()
        if len(heaters) == 1:
            return max(abs(houses[0] - heaters[0]), abs(houses[-1] - heaters[0]))

        max_value = -1
        f, s, ind_heat = heaters[0], heaters[1], 2
        for i in range(len(houses)):
            while houses[i] > s and ind_heat < len(heaters):
                f, s = s, heaters[ind_heat]
                ind_heat += 1
            max_value = max(max_value, min(abs(houses[i] - f), abs(houses[i] - s)))
        return max_value

    def findRadius(self, houses: List[int], heaters: List[int]) -> int:
        houses.sort()
        heaters.sort()
        res = 0
        # For each house, find the closest heater to the left and the right
        for house in houses:
            left = bisect.bisect_right(heaters, house) - 1
            right = bisect.bisect_left(heaters, house)
            # If the house is to the left of all heaters, use the closest heater to the left
            if left < 0:
                res = max(res, heaters[0] - house)
            # If the house is to the right of all heaters, use the closest heater to the right
            elif right >= len(heaters):
                res = max(res, house - heaters[-1])
            # If the house is between two heaters, use the closer of the two
            else:
                res = max(res, min(house - heaters[left], heaters[right] - house))
        # Return the result
        return res

