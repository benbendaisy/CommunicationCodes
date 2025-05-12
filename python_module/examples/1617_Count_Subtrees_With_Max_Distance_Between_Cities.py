class Solution:
    """
    There are n cities numbered from 1 to n. You are given an array edges of size n-1, where edges[i] = [ui, vi] represents a bidirectional edge between cities ui and vi. There exists a unique path between each pair of cities. In other words, the cities form a tree.

    A subtree is a subset of cities where every city is reachable from every other city in the subset, where the path between each pair passes through only the cities from the subset. Two subtrees are different if there is a city in one subtree that is not present in the other.

    For each d from 1 to n-1, find the number of subtrees in which the maximum distance between any two cities in the subtree is equal to d.

    Return an array of size n-1 where the dth element (1-indexed) is the number of subtrees in which the maximum distance between any two cities is equal to d.

    Notice that the distance between the two cities is the number of edges in the path between them.

    Example 1:

    Input: n = 4, edges = [[1,2],[2,3],[2,4]]
    Output: [3,4,0]
    Explanation:
    The subtrees with subsets {1,2}, {2,3} and {2,4} have a max distance of 1.
    The subtrees with subsets {1,2,3}, {1,2,4}, {2,3,4} and {1,2,3,4} have a max distance of 2.
    No subtree has two nodes where the max distance between them is 3.
    Example 2:

    Input: n = 2, edges = [[1,2]]
    Output: [1]
    Example 3:

    Input: n = 3, edges = [[1,2],[2,3]]
    Output: [2,1]
    """
    def countSubgraphsForEachDiameter1(self, n: int, edges: List[List[int]]) -> List[int]:
        graph = [[] for _ in range(n)]                              # 建图
        for u, v in edges:
            graph[u - 1].append(v - 1)
            graph[v - 1].append(u - 1)

        def dfs(mask, u):
            nonlocal visited, diameter
            visited |= 1 << u                                       # 标记 u 访问过
            u_len = 0                                               # u 节点的最大路径长度
            for v in graph[u]:                                      # 遍历 u 节点的相邻节点
                if (visited >> v) & 1 == 0 and mask >> v & 1:       # v 没有访问过，且在子集中
                    v_len = dfs(mask, v)                            # 相邻节点的最大路径长度
                    diameter = max(diameter, u_len + v_len + 1)     # 维护最大路径长度
                    u_len = max(u_len, v_len + 1)                   # 更新 u 节点的最大路径长度
            return u_len
        
        ans = [0 for _ in range(n - 1)]

        for mask in range(3, 1 << n):                               # 二进制枚举子集
            if mask & (mask - 1) == 0:                              # 子集至少需要两个点
                continue
            visited = 0
            diameter = 0
            u = mask.bit_length() - 1        
            dfs(mask, u)                                            # 在子集 mask 中递归求树的直径
            if visited == mask:
                ans[diameter - 1] += 1
        return ans
    
    def countSubgraphsForEachDiameter2(self, n: int, edges: List[List[int]]) -> List[int]:
        if not edges:
            return []
        graph = defaultdict(list)
        for u, v in edges:
            graph[u - 1].append(v - 1)
            graph[v - 1].append(u - 1)
        
        def helper(mask: int, node: int):
            self.visited |= 1 << node
            u_len = 0
            for neighbor in graph[node]:
                if (self.visited >> neighbor) & 1 == 0 and mask >> neighbor & 1 == 1:
                    v_len = helper(mask, neighbor)
                    self.diameter = max(self.diameter, u_len + v_len + 1)
                    u_len = max(u_len, v_len + 1)
            return u_len
        
        res = [0 for _ in range(n - 1)]
        for mask in range(3, 1 << n):
            if mask & (mask - 1) == 0:
                continue
            
            self.diameter = 0
            node = mask.bit_length() - 1
            self.visited = 0
            helper(mask, node)
            if self.visited == mask:
                res[self.diameter - 1] += 1
        return res
    
    def countSubgraphsForEachDiameter3(self, n: int, edges: List[List[int]]) -> List[int]:
        if not edges:
            return []
        graph = defaultdict(list)
        for u, v in edges:
            graph[u - 1].append(v - 1)
            graph[v - 1].append(u - 1)
        
        def helper(sub_tree: int, node: int):
            self.visited |= 1 << node
            u_len = 0
            for neighbor in graph[node]:
                if (self.visited >> neighbor) & 1 == 0 and sub_tree >> neighbor & 1 == 1: # check if neighbor in the sub_tree and not visited
                    v_len = helper(sub_tree, neighbor) # check neighbor's diameter
                    self.diameter = max(self.diameter, u_len + v_len + 1) # get the max diameter
                    u_len = max(u_len, v_len + 1) # update the max path
            return u_len
        
        res = [0 for _ in range(n - 1)]
        for sub_tree in range(3, 1 << n): # pick sub_trees
            if sub_tree & (sub_tree - 1) == 0: # sub_trees must have more than 1 nodes
                continue
            
            self.diameter = 0
            node = sub_tree.bit_length() - 1
            self.visited = 0
            helper(sub_tree, node)
            if self.visited == sub_tree:
                res[self.diameter - 1] += 1
        return res