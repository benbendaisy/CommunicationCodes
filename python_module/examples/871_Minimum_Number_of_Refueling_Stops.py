import heapq
import math
from typing import List


class Solution:
    """
        A car travels from a starting position to a destination which is target miles east of the starting position.

        There are gas stations along the way. The gas stations are represented as an array stations where stations[i] = [positioni, fueli] indicates that the ith gas station is positioni miles east of the starting position and has fueli liters of gas.

        The car starts with an infinite tank of gas, which initially has startFuel liters of fuel in it. It uses one liter of gas per one mile that it drives. When the car reaches a gas station, it may stop and refuel, transferring all the gas from the station into the car.

        Return the minimum number of refueling stops the car must make in order to reach its destination. If it cannot reach the destination, return -1.

        Note that if the car reaches a gas station with 0 fuel left, the car can still refuel there. If the car reaches the destination with 0 fuel left, it is still considered to have arrived.

        Example 1:

        Input: target = 1, startFuel = 1, stations = []
        Output: 0
        Explanation: We can reach the target without refueling.
        Example 2:

        Input: target = 100, startFuel = 1, stations = [[10,100]]
        Output: -1
        Explanation: We can not reach the target (or even the first gas station).
        Example 3:

        Input: target = 100, startFuel = 10, stations = [[10,60],[20,30],[30,30],[60,40]]
        Output: 2
        Explanation: We start with 10 liters of fuel.
        We drive to position 10, expending 10 liters of fuel.  We refuel from 0 liters to 60 liters of gas.
        Then, we drive from position 10 to position 60 (expending 50 liters of fuel),
        and refuel from 10 liters to 50 liters of gas.  We then drive to and reach the target.
        We made 2 refueling stops along the way, so we return 2.

        Constraints:

        1 <= target, startFuel <= 109
        0 <= stations.length <= 500
        0 <= positioni <= positioni+1 < target
        1 <= fueli < 109
    """
    def minRefuelStops1(self, target: int, startFuel: int, stations: List[List[int]]) -> int:
        dp = [startFuel] + [0] * len(stations)
        for i, (location, capacity) in enumerate(stations):
            for j in range(0, -1, -1):
                if dp[j] >= location:
                    dp[j + 1] = max(dp[j + 1], dp[j] + capacity)

        for i, d in enumerate(dp):
            if d >= target:
                return i

        return -1

    def minRefuelStops2(self, target: int, startFuel: int, stations: List[List[int]]) -> int:
        maxHeap = [] # A maxheap is simulated using negative values
        stations.append((target, math.inf)) # add the target into station so that we can check if we can reach
        ans = prev = 0

        # use startFuel as tank to check we have enough gas
        for location, capacity in stations:
            startFuel -= location - prev
            while maxHeap and startFuel < 0:
                startFuel += -heapq.heappop(maxHeap)
                ans += 1
            if startFuel < 0: # check if the startFuel (tank) has enough fuel
                return -1
            heapq.heappush(maxHeap, -capacity)
            prev = location # refuel the gas
        return ans
    
    def minRefuelStops3(self, target: int, startFuel: int, stations: List[List[int]]) -> int:
        # Early return if we can reach the target directly
        if startFuel >= target:
            return 0
        
        # Early return if no stations and we can't reach target
        if not stations:
            return -1
        
        n = len(stations)
        
        @cache
        def helper(position: int, fuel: int, idx: int):
            # If we have enough fuel to reach the target
            if fuel >= target - position:
                return 0
            
            # If we've considered all stations and still can't reach
            if idx == n:
                return float('inf')
            
            # Current station's position and fuel
            station_pos, station_fuel = stations[idx]
            
            # If we can't reach the current station
            if position + fuel < station_pos:
                return float('inf')
            
            # Option 1: Skip this station
            skip = helper(position, fuel, idx + 1)
            
            # Option 2: Refuel at this station
            # When we refuel, we're at the station's position with
            # our remaining fuel plus the station's fuel
            remaining_fuel = fuel - (station_pos - position)
            refuel = 1 + helper(station_pos, remaining_fuel + station_fuel, idx + 1)
            
            return min(skip, refuel)
        
        result = helper(0, startFuel, 0)
        return -1 if result == float('inf') else result
    
    def minRefuelStops4(self, target: int, startFuel: int, stations: List[List[int]]) -> int:
        if startFuel >= target:
            return 0
        if not stations:
            return -1
        
        n = len(stations)
        @cache
        def helper(position: int, fuel: int, idx: int):
            if fuel >= target - position:
                return 0
            
            if idx == n:
                return float('inf')
            
            cur_pos, cur_fuel = stations[idx]
            if position + fuel < cur_pos:
                return float('inf')
            
            skip = helper(position, fuel, idx + 1)

            remain_fuel = fuel - (cur_pos - position)
            refuel = 1 + helper(cur_pos, remain_fuel + cur_fuel, idx + 1)
            return min(skip, refuel)
        res = helper(0, startFuel, 0)
        return -1 if res == float('inf') else res
    
    def minRefuelStops(self, target: int, startFuel: int, stations: List[List[int]]) -> int:
        # Early return if we can reach target directly
        if startFuel >= target:
            return 0
        
        # Max heap to store fuel amounts from stations we've passed
        max_heap = []
        
        current_fuel = startFuel
        stops = 0
        i = 0
        
        while current_fuel < target:
            # Add all reachable stations to our heap
            while i < len(stations) and stations[i][0] <= current_fuel:
                # Push negative value for max heap (Python only has min heap)
                heapq.heappush(max_heap, -stations[i][1])
                i += 1
            
            # If no stations are available to refuel
            if not max_heap:
                return -1
            
            # Refuel at the station with maximum fuel
            current_fuel += -heapq.heappop(max_heap)
            stops += 1
        
        return stops

