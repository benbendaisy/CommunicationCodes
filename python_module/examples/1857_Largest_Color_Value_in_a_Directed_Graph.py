from collections import defaultdict
from typing import List


class Solution:
    """
        There is a directed graph of n colored nodes and m edges. The nodes are numbered from 0 to n - 1.

        You are given a string colors where colors[i] is a lowercase English letter representing the color of the ith node in this graph (0-indexed). You are also given a 2D array edges where edges[j] = [aj, bj] indicates that there is a directed edge from node aj to node bj.

        A valid path in the graph is a sequence of nodes x1 -> x2 -> x3 -> ... -> xk such that there is a directed edge from xi to xi+1 for every 1 <= i < k. The color value of the path is the number of nodes that are colored the most frequently occurring color along that path.

        Return the largest color value of any valid path in the given graph, or -1 if the graph contains a cycle.

        Example 1:

        Input: colors = "abaca", edges = [[0,1],[0,2],[2,3],[3,4]]
        Output: 3
        Explanation: The path 0 -> 2 -> 3 -> 4 contains 3 nodes that are colored "a" (red in the above image).
        Example 2:

        Input: colors = "a", edges = [[0,0]]
        Output: -1
        Explanation: There is a cycle from 0 to 0.
    """
    def largestPathValue1(self, colors: str, edges: List[List[int]]) -> int:
        n, k = len(colors), 26
        in_degrees = [0] * n
        graph = [[] for _ in range(n)]
        for u, v in edges:
            graph[u].append(v)
            in_degrees[v] += 1
        zero_in_degrees = set(i for i in range(n) if in_degrees[i] == 0)
        counts = [[0] * k for _ in range(n)]
        for i, c in enumerate(colors):
            counts[i][ord(c) - ord('a')] += 1
        max_cnt, visited = 0, 0
        while zero_in_degrees:
            u = zero_in_degrees.pop()
            visited += 1
            for v in graph[u]:
                for i in range(k):
                    counts[v][i] = max(counts[v][i], counts[u][i] + (ord(colors[v]) - ord('a') == i))
                in_degrees[v] -= 1
                if in_degrees[v] == 0:
                    zero_in_degrees.add(v)
            max_cnt = max(max_cnt, max(counts[u]))
        return max_cnt if visited == n else -1

    def largestPathValue2(self, colors: str, edges: List[List[int]]) -> int:
        n = len(colors)
        graph = defaultdict(set)
        in_degrees = [0] * n
        for u, v in edges:
            graph[u].add(v)
            in_degrees[v] += 1
        que = [i for i in range(n) if in_degrees[i] == 0]
        #max freq of each colors over all paths ending at i
        colors_dict = {i : defaultdict(int) for i in range(n)}
        visited_cnt, ans = 0, 0
        while que:
            node = que.pop()
            colors_dict[node][colors[node]] += 1
            ans = max(ans, max(colors_dict[node].values()))
            visited_cnt += 1
            for v in graph[node]:
                for x in colors_dict[node]:
                    colors_dict[v][x] = max(colors_dict[v][x], colors_dict[node][x])
                in_degrees[v] -= 1
                if in_degrees[v] == 0:
                    que.append(v)
        return ans if visited_cnt == n else -1
    
    def largestPathValue3(self, colors: str, edges: List[List[int]]) -> int:
        n = len(colors)
        graph = defaultdict(list)
        indegree = [0] * n
        
        # Build graph and compute in-degrees
        for u, v in edges:
            graph[u].append(v)
            indegree[v] += 1
        
        # Topological sorting using Kahn’s Algorithm (BFS)
        queue = deque()
        dp = [[0] * 26 for _ in range(n)]  # DP table to store max frequency of each color at each node
        visited_count = 0
        
        for i in range(n):
            if indegree[i] == 0:
                queue.append(i)
                dp[i][ord(colors[i]) - ord('a')] = 1  # Initialize color count for starting nodes

        topological_order = []
        
        while queue:
            node = queue.popleft()
            topological_order.append(node)
            visited_count += 1

            for neighbor in graph[node]:
                for c in range(26):  # Propagate color frequencies
                    dp[neighbor][c] = max(dp[neighbor][c], dp[node][c] + (1 if c == ord(colors[neighbor]) - ord('a') else 0))

                indegree[neighbor] -= 1
                if indegree[neighbor] == 0:
                    queue.append(neighbor)
        
        # If not all nodes were visited, a cycle exists
        if visited_count < n:
            return -1  # Cycle detected
        
        # Get the largest color frequency in any node
        return max(max(row) for row in dp)
    
    def largestPathValue4(self, colors: str, edges: List[List[int]]) -> int:
        n = len(colors)
        graph = defaultdict(list)
        indegree = [0] * n
        
        # Build graph and compute in-degrees
        for u, v in edges:
            graph[u].append(v)
            indegree[v] += 1
        
        # Initialize DP table for color counts
        dp = [[0] * 26 for _ in range(n)]
        visited_count = 0
        
        # Initialize queue with nodes having 0 indegree
        queue = deque([i for i in range(n) if indegree[i] == 0])
        
        # Process nodes in topological order
        while queue:
            node = queue.popleft()
            color_idx = ord(colors[node]) - ord('a')
            dp[node][color_idx] += 1  # Count this node's color
            visited_count += 1
            
            for neighbor in graph[node]:
                # Update DP values more efficiently
                for c in range(26):
                    dp[neighbor][c] = max(dp[neighbor][c], dp[node][c])
                
                indegree[neighbor] -= 1
                if indegree[neighbor] == 0:
                    queue.append(neighbor)
        
        # Check for cycles
        if visited_count < n:
            return -1
        
        # Find maximum color frequency
        max_freq = 0
        for i in range(n):
            max_freq = max(max_freq, max(dp[i]))
        
        return max_freq

    def largestPathValue5(self, colors: str, edges: List[List[int]]) -> int:
        n = len(colors)
        graph = defaultdict(list)
        in_degree = defaultdict(int)
        for u, v in edges:
            graph[u].append(v)
            in_degree[v] += 1
        
        que = deque([node for node in range(n) if in_degree[node] == 0])
        dp = [[0] * 26 for _ in range(n)]
        visited_cnt = 0
        while que:
            node = que.popleft()
            color_idx = ord(colors[node]) - ord('a')
            dp[node][color_idx] += 1
            visited_cnt += 1
            for neighbor in graph[node]:
                for c in range(26):
                    dp[neighbor][c] = max(dp[neighbor][c], dp[node][c])
                in_degree[neighbor] -= 1
                if in_degree[neighbor] == 0:
                    que.append(neighbor)
        if visited_cnt < n:
            return -1
        
        max_freq = 0
        for i in range(n):
            max_freq = max(max_freq, max(dp[i]))
        return max_freq
    
    def largestPathValue6(self, colors: str, edges: List[List[int]]) -> int:
        n = len(colors)
        graph, in_degree = defaultdict(list), [0] * n
        for u, v in edges:
            graph[u].append(v)
            in_degree[v] += 1
        
        que = [i for i in range(n) if in_degree[i] == 0]
        # max freq of each colors over all paths ending at i
        colors_dict = {i: defaultdict(int) for i in range(n)}
        visited_cnt, res = 0, 0
        while que:
            node = que.pop()
            colors_dict[node][colors[node]] += 1
            res = max(res, colors_dict[node][colors[node]])
            visited_cnt += 1
            for neighbor in graph[node]:
                for x in colors_dict[node]:
                    colors_dict[neighbor][x] = max(colors_dict[neighbor][x], colors_dict[node][x])
                in_degree[neighbor] -= 1
                if in_degree[neighbor] == 0:
                    que.append(neighbor)
        return res if visited_cnt == n else -1
    
    def largestPathValue7(self, colors: str, edges: List[List[int]]) -> int:
        if not colors:
            return 0
        
        n = len(colors)
        graph, in_degree = defaultdict(list), [0] * n
        for u, v in edges:
            graph[u].append(v)
            in_degree[v] += 1
        
        que = [i for i in range(n) if in_degree[i] == 0]
        color_dict = [defaultdict(int) for _ in range(n)]
        visited_node, max_color = 0, 0
        while que:
            node = que.pop()
            cur_color = colors[node]
            color_dict[node][cur_color] += 1
            max_color = max(max_color, color_dict[node][cur_color])
            visited_node += 1
            for neighbor in graph[node]:
                for cl in color_dict[node]:
                    color_dict[neighbor][cl] = max(color_dict[neighbor][cl], color_dict[node][cl])
                in_degree[neighbor] -= 1
                if in_degree[neighbor] == 0:
                    que.append(neighbor)
        
        return max_color if visited_node == n else -1

if __name__ == "__main__":
    colors = "abaca"
    edges = [[0,1],[0,2],[2,3],[3,4]]
    solution = Solution()
    ret = solution.largestPathValue(colors, edges)
    print(ret)

