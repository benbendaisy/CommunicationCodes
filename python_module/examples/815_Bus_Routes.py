from typing import List


class Solution:
    """
    You are given an array routes representing bus routes where routes[i] is a bus route that the ith bus repeats forever.

    For example, if routes[0] = [1, 5, 7], this means that the 0th bus travels in the sequence 1 -> 5 -> 7 -> 1 -> 5 -> 7 -> 1 -> ... forever.
    You will start at the bus stop source (You are not on any bus initially), and you want to go to the bus stop target. You can travel between bus stops by buses only.

    Return the least number of buses you must take to travel from source to target. Return -1 if it is not possible.

    Example 1:

    Input: routes = [[1,2,7],[3,6,7]], source = 1, target = 6
    Output: 2
    Explanation: The best strategy is take the first bus to the bus stop 7, then take the second bus to the bus stop 6.
    Example 2:

    Input: routes = [[7,12],[4,5,15],[6],[15,19],[9,12,13]], source = 15, target = 12
    Output: -1
    """
    def numBusesToDestination1(self, routes: List[List[int]], source: int, target: int) -> int:
        if source == target:
            return 0
        max_stop = max(max(route) for route in routes)
        if max_stop < target:
            return -1
        
        min_buses = [float('inf')] * (max_stop + 1)
        min_buses[source] = 0
        flag = True
        while flag:
            flag = False
            for route in routes:
                mini = float('inf')
                for stop in route:
                    mini = min(mini, min_buses[stop])
                mini += 1
                for stop in route:
                    if min_buses[stop] > mini:
                        min_buses[stop] = mini
                        flag = True
        return min_buses[target] if min_buses[target] < float('inf') else -1
    
    def numBusesToDestination(self, routes: List[List[int]], source: int, target: int) -> int:
        if source == target:
            return 0
        graph = defaultdict(set)
        for route_id, stops in enumerate(routes):
            for stop in stops:
                graph[stop].add(route_id)

        que = deque([(source, 0)])
        visited_stops = set([source])
        visited_routes = set()
        while que:
            stop, changes = que.popleft()
            if stop == target:
                return changes
            for route_id in graph[stop]:
                if route_id not in visited_routes:
                    visited_routes.add(route_id)

                    for stop in routes[route_id]:
                        if stop not in visited_stops:
                            visited_stops.add(stop)
                            que.append((stop, changes + 1))
        return -1