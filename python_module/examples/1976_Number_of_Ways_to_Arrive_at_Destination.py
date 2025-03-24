class Solution:
    """
    You are in a city that consists of n intersections numbered from 0 to n - 1 with bi-directional roads between some intersections. The inputs are generated such that you can reach any intersection from any other intersection and that there is at most one road between any two intersections.

    You are given an integer n and a 2D integer array roads where roads[i] = [ui, vi, timei] means that there is a road between intersections ui and vi that takes timei minutes to travel. You want to know in how many ways you can travel from intersection 0 to intersection n - 1 in the shortest amount of time.

    Return the number of ways you can arrive at your destination in the shortest amount of time. Since the answer may be large, return it modulo 109 + 7.

    Example 1:


    Input: n = 7, roads = [[0,6,7],[0,1,2],[1,2,3],[1,3,3],[6,3,3],[3,5,1],[6,5,1],[2,5,1],[0,4,5],[4,6,2]]
    Output: 4
    Explanation: The shortest amount of time it takes to go from intersection 0 to intersection 6 is 7 minutes.
    The four ways to get there in 7 minutes are:
    - 0 ➝ 6
    - 0 ➝ 4 ➝ 6
    - 0 ➝ 1 ➝ 2 ➝ 5 ➝ 6
    - 0 ➝ 1 ➝ 3 ➝ 5 ➝ 6
    Example 2:

    Input: n = 2, roads = [[1,0,10]]
    Output: 1
    Explanation: There is only one way to go from intersection 0 to intersection 1, and it takes 10 minutes.
    """
    def countPaths1(self, n: int, roads: List[List[int]]) -> int:
        def countPaths(self, n: int, roads: List[List[int]]) -> int:
            if not roads:
                return 0
            graph = defaultdict(list)
            for u, v, t in roads:
                graph[u].append((v, t))
                graph[v].append((u, t))
            
            @cache
            def helper(node: int, mask: int) -> int:
                if node == n - 1:
                    return 0
                
                shortest_time = float('inf')
                for neighbor, time in graph[node]:
                    if (1 << neighbor) & mask != 0:
                        continue
                    shortest_time = min(shortest_time, time + helper(neighbor, (1 << neighbor) | mask))
                return shortest_time
            
            shortest_time = helper(0, 0)
            @cache
            def count_pathes(node: int, mask: int, running_time: int) -> int:
                if node == n - 1:
                    return 1 if running_time == shortest_time else 0
                
                cnt = 0
                for neighbor, time in graph[node]:
                    if (1 << neighbor) & mask != 0:
                        continue
                    cnt += count_pathes(neighbor, (1 << neighbor) | mask, time + running_time)
                return cnt
            return count_pathes(0, 0, 0)
        
    def countPaths2(self, n: int, roads: List[List[int]]) -> int:
        mod = 10**9 + 7
    
        # Step 1: Build the adjacency list
        graph = defaultdict(list)
        for u, v, time in roads:
            graph[u].append((v, time))
            graph[v].append((u, time))
        
        # Step 2: Use Dijkstra's Algorithm to find shortest path times
        min_time = [float('inf')] * n
        ways = [0] * n
        min_time[0] = 0
        ways[0] = 1
        
        min_heap = [(0, 0)]  # (time, node)
        
        while min_heap:
            current_time, node = heappop(min_heap)
            
            if current_time > min_time[node]:
                continue  # Ignore outdated entries
            
            for neighbor, travel_time in graph[node]:
                new_time = current_time + travel_time
                
                if new_time < min_time[neighbor]:
                    min_time[neighbor] = new_time
                    ways[neighbor] = ways[node]
                    heappush(min_heap, (new_time, neighbor))
                elif new_time == min_time[neighbor]:
                    ways[neighbor] = (ways[neighbor] + ways[node])
        
        return ways[n - 1] % mod
    
    def countPaths(self, n: int, roads: List[List[int]]) -> int:
        mod = 10 ** 9 + 7
        graph = defaultdict(list)
        for u, v, t in roads:
            graph[u].append((v, t))
            graph[v].append((u, t))

        ways = [0] * n
        ways[0] = 1
        min_time = [float('inf')] * n
        min_time[0] = 0
        min_heap = [(0, 0)]

        while min_heap:
            current_time, node = heapq.heappop(min_heap)
            if current_time > min_time[node]:
                continue
            
            for neighbor, time in graph[node]:
                new_time = current_time + time
                if new_time < min_time[neighbor]:
                    min_time[neighbor] = new_time
                    ways[neighbor] = ways[node]
                    heapq.heappush(min_heap, (new_time, neighbor))
                elif new_time == min_time[neighbor]:
                    ways[neighbor] = ways[neighbor] + ways[node]
        return ways[n - 1] % mod