class UnionFind:
    def __init__(self, n: int):
        self.parent = [*range(n)]
        self.rank = [1] * n
        self.weight = [-1] * n
               
    def find(self, x: int) -> int:
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]

    def union(self, x: int, y: int, w: int) -> None:
        x, y = self.find(x), self.find(y)
        if x == y:
            self.weight[x] &= w
            return
        if self.rank[x] < self.rank[y]:
            self.parent[x] = y
            self.weight[y] &= self.weight[x] & w
        else:
            self.parent[y] = x
            self.weight[x] &= self.weight[y] & w
            if self.rank[x] == self.rank[y]:
                self.rank[x] += 1
class Solution:
    """
    There is an undirected weighted graph with n vertices labeled from 0 to n - 1.

    You are given the integer n and an array edges, where edges[i] = [ui, vi, wi] indicates that there is an edge between vertices ui and vi with a weight of wi.

    A walk on a graph is a sequence of vertices and edges. The walk starts and ends with a vertex, and each edge connects the vertex that comes before it and the vertex that comes after it. It's important to note that a walk may visit the same edge or vertex more than once.

    The cost of a walk starting at node u and ending at node v is defined as the bitwise AND of the weights of the edges traversed during the walk. In other words, if the sequence of edge weights encountered during the walk is w0, w1, w2, ..., wk, then the cost is calculated as w0 & w1 & w2 & ... & wk, where & denotes the bitwise AND operator.

    You are also given a 2D array query, where query[i] = [si, ti]. For each query, you need to find the minimum cost of the walk starting at vertex si and ending at vertex ti. If there exists no such walk, the answer is -1.

    Return the array answer, where answer[i] denotes the minimum cost of a walk for query i.

    Example 1:

    Input: n = 5, edges = [[0,1,7],[1,3,7],[1,2,1]], query = [[0,3],[3,4]]

    Output: [1,-1]

    Explanation:

    To achieve the cost of 1 in the first query, we need to move on the following edges: 0->1 (weight 7), 1->2 (weight 1), 2->1 (weight 1), 1->3 (weight 7).

    In the second query, there is no walk between nodes 3 and 4, so the answer is -1.

    Example 2:

    Input: n = 3, edges = [[0,2,7],[0,1,15],[1,2,6],[1,2,1]], query = [[1,2]]

    Output: [0]

    Explanation:

    To achieve the cost of 0 in the first query, we need to move on the following edges: 1->2 (weight 1), 2->1 (weight 6), 1->2 (weight 1).
    """
    def minimumCost1(self, n: int, edges: List[List[int]], query: List[List[int]]) -> List[int]:
        """
        This solution uses a recursive DFS approach to find the minimum cost of a walk from the source to the target node.
        The operation is adding instead of bitwise AND.
        """
        graph = defaultdict(list)
        for u, v, w in edges:
            graph[u].append((v, w))
            graph[v].append((u, w))
        
        @cache
        def helper(node: int, parent: int, target: int) -> int:
            if node == target:
                return 0
            min_cost = float("inf")
            for neighbor, weight in graph[node]:
                if neighbor == parent:
                    continue
                min_cost = min(min_cost, weight + helper(neighbor, node, target))
            return min_cost
        
        res = []
        for q in query:
            r = helper(q[0], -1, q[1])
            res.append(-1 if r == float('inf') else r)
        return res
    
    def minimumCost2(self, n: int, edges: List[List[int]], query: List[List[int]]) -> List[int]:
        uf = UnionFind(n)
        for u, v, w in edges:
            uf.union(u, v, w)
        ans = []
        for u, v in query:
            u, v = uf.find(u), uf.find(v)
            ans.append(uf.weight[u] if u == v else -1)
        return ans
    
    def minimumCost(self, n: int, edges: List[List[int]], query: List[List[int]]) -> List[int]:
        class UnionFind:
            def __init__(self, n: int):
                self.parent = [i for i in range(n)]
                self.rank = [1] * n
                self.weight = [-1] * n
            
            def find(self, x: int) -> int:
                if self.parent[x] != x:
                    self.parent[x] = self.find(self.parent[x])
                return self.parent[x]
            
            def union(self, x: int, y: int, w: int) -> None:
                x, y = self.find(x), self.find(y)
                if x == y:
                    self.weight[x] &= w
                    return
                if self.rank[x] < self.rank[y]:
                    self.parent[x] = self.parent[y]
                    self.weight[y] &= self.weight[x] & w
                else:
                    self.parent[y] = self.parent[x]
                    self.weight[x] &= self.weight[y] & w
                if self.rank[x] == self.rank[y]:
                    self.rank[x] += 1
        uf = UnionFind(n)
        for u, v, w in edges:
            uf.union(u, v, w)
        
        res = []
        for u, v in query:
            u, v = uf.find(u), uf.find(v)
            res.append(uf.weight[u] if u == v else -1)
        return res
