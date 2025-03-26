from typing import List


class Solution:
    """
    You are given a positive integer n representing the number of nodes in a tree, numbered from 0 to n - 1 (inclusive). You are also given a 2D integer array edges of length n - 1, where edges[i] = [node1i, node2i] denotes that there is a bidirectional edge connecting node1i and node2i in the tree.

    You are given a 0-indexed integer array query of length m where query[i] = [starti, endi, nodei] means that for the ith query, you are tasked with finding the node on the path from starti to endi that is closest to nodei.

    Return an integer array answer of length m, where answer[i] is the answer to the ith query.

    Example 1:

    Input: n = 7, edges = [[0,1],[0,2],[0,3],[1,4],[2,5],[2,6]], query = [[5,3,4],[5,3,6]]
    Output: [0,2]
    Explanation:
    The path from node 5 to node 3 consists of the nodes 5, 2, 0, and 3.
    The distance between node 4 and node 0 is 2.
    Node 0 is the node on the path closest to node 4, so the answer to the first query is 0.
    The distance between node 6 and node 2 is 1.
    Node 2 is the node on the path closest to node 6, so the answer to the second query is 2.
    Example 2:


    Input: n = 3, edges = [[0,1],[1,2]], query = [[0,1,2]]
    Output: [1]
    Explanation:
    The path from node 0 to node 1 consists of the nodes 0, 1.
    The distance between node 2 and node 1 is 1.
    Node 1 is the node on the path closest to node 2, so the answer to the first query is 1.
    Example 3:

    Input: n = 3, edges = [[0,1],[1,2]], query = [[0,0,0]]
    Output: [0]
    Explanation:
    The path from node 0 to node 0 consists of the node 0.
    Since 0 is the only node on the path, the answer to the first query is 0.
    """
    def closestNode1(self, n: int, edges: List[List[int]], query: List[List[int]]) -> List[int]:
        graph = defaultdict(list)
        for i, j in edges:
            graph[i].append(j)
            graph[j].append(i)
        
        def dfs(start, end):
            if start == end:
                return True
            visited.add(start)
            for neighbor in graph[start]:
                if neighbor not in visited:
                    stack.append(neighbor)
                if dfs(neighbor, end):
                    return True
                stack.remove(neighbor)
        
        def bfs(res, path):
            visited = set()
            visited.add(res[0])
            while res:
                node = res.pop(0)
                if node in path:
                    return node
                for neighbor in graph[node]:
                    if neighbor not in visited:
                        visited.add(neighbor)
                        res.append(neighbor)
        
        res = []
        for q in query:
            visited = set()
            stack = [q[0]]
            dfs(q[0], q[1])

            if q[2] in stack:
                res.append(q[2])
                continue
            res.append(bfs([q[2]], stack))
        return res
    
    def closestNode2(self, n: int, edges: List[List[int]], query: List[List[int]]) -> List[int]:
        """
        Time Limit Exceeded
        """
        if not query:
            return []
        
        graph = defaultdict(list)
        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)
        
        def helper(node: int, end: int, mask: int, path: list) -> list:
            if node == end:
                return path

            for neighbor in graph[node]:
                if (1 << neighbor) & mask != 0:
                    continue
                res = helper(neighbor, end, mask | (1 << neighbor), path + [neighbor])
                if res:
                    return res
            return []
        res = []
        for q in query:
            path = helper(q[0], q[1], 1 << q[0], [q[0]])
            if q[2] in path:
                res.append(q[2])
                continue
            que = deque([(node, node) for node in path])
            while que:
                close_node, node = que.popleft()
                if node == q[2]:
                    res.append(close_node)
                    break
                for neighbor in graph[node]:
                    que.append((close_node, neighbor))
        return res

    def closestNode3(self, n: int, edges: List[List[int]], query: List[List[int]]) -> List[int]:
        if not query:
            return []
        
        # Build the graph
        graph = defaultdict(list)
        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)

        # BFS to find shortest path from start to end
        def bfs_path(start, end):
            parent = {start: None}
            queue = deque([start])
            
            while queue:
                node = queue.popleft()
                if node == end:
                    break
                for neighbor in graph[node]:
                    if neighbor not in parent:
                        parent[neighbor] = node
                        queue.append(neighbor)
            
            # Reconstruct path
            path = set()
            while end is not None:
                path.add(end)
                end = parent[end]
            
            return path
        
        result = []
        for start, end, target in query:
            path_nodes = bfs_path(start, end)  # Get set of path nodes
            if target in path_nodes:
                result.append(target)
            else:
                # Find the closest node in path using BFS
                queue = deque([target])
                visited = set([target])
                
                while queue:
                    node = queue.popleft()
                    if node in path_nodes:
                        result.append(node)
                        break
                    for neighbor in graph[node]:
                        if neighbor not in visited:
                            visited.add(neighbor)
                            queue.append(neighbor)
        
        return result
    
    def closestNode4(self, n: int, edges: List[List[int]], query: List[List[int]]) -> List[int]:
        if not query:
            return []
        
        graph = defaultdict(list)
        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)
        
        def helper(node: int, end: int, mask: int, path: list) -> list:
            if node == end:
                return path

            for neighbor in graph[node]:
                if (1 << neighbor) & mask != 0:
                    continue
                res = helper(neighbor, end, mask | (1 << neighbor), path + [neighbor])
                if res:
                    return res
            return []
        res = []
        for q in query:
            path = helper(q[0], q[1], 1 << q[0], [q[0]])
            if q[2] in path:
                res.append(q[2])
                continue
            que = deque([q[2]])
            seen = set()
            while que:
                node = que.popleft()
                seen.add(node)
                if node in path:
                    res.append(node)
                    break
                for neighbor in graph[node]:
                    if neighbor not in seen:
                        que.append(neighbor)
        return res