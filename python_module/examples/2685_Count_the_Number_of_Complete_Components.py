class Solution:
    """
    You are given an integer n. There is an undirected graph with n vertices, numbered from 0 to n - 1. You are given a 2D integer array edges where edges[i] = [ai, bi] denotes that there exists an undirected edge connecting vertices ai and bi.

    Return the number of complete connected components of the graph.

    A connected component is a subgraph of a graph in which there exists a path between any two vertices, and no vertex of the subgraph shares an edge with a vertex outside of the subgraph.

    A connected component is said to be complete if there exists an edge between every pair of its vertices.

    Example 1:

    Input: n = 6, edges = [[0,1],[0,2],[1,2],[3,4]]
    Output: 3
    Explanation: From the picture above, one can see that all of the components of this graph are complete.
    Example 2:

    Input: n = 6, edges = [[0,1],[0,2],[1,2],[3,4],[3,5]]
    Output: 1
    Explanation: The component containing vertices 0, 1, and 2 is complete since there is an edge between every pair of two vertices. On the other hand, the component containing vertices 3, 4, and 5 is not complete since there is no edge between vertices 4 and 5. Thus, the number of complete components in this graph is 1.
    """
    def countCompleteComponents1(self, n: int, edges: List[List[int]]) -> int:
        # Step 1: Build adjacency list representation of the graph
        graph = defaultdict(set)
        for u, v in edges:
            graph[u].add(v)
            graph[v].add(u)
        
        visited = set()
        complete_components = 0
        
        # Step 2: DFS to find connected components
        def dfs(node, component):
            stack = [node]
            while stack:
                curr = stack.pop()
                for neighbor in graph[curr]:
                    if neighbor not in visited:
                        visited.add(neighbor)
                        component.add(neighbor)
                        stack.append(neighbor)
            return component
        
        # Step 3: Check completeness condition
        for node in range(n):
            if node not in visited:
                visited.add(node)
                component = dfs(node, component)
                size = len(component)
                is_complete = all(len(graph[v]) == size - 1 for v in component)
                if is_complete:
                    complete_components += 1
        
        return complete_components

    def countCompleteComponents(self, n: int, edges: List[List[int]]) -> int:
        graph = defaultdict(list)
        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)
        visited = set()

        def helper(node: int) -> set:
            stack, component = [node], {node}
            while stack:
                curr = stack.pop()
                for neighbor in graph[curr]:
                    if neighbor not in visited:
                        visited.add(neighbor)
                        component.add(neighbor)
                        stack.append(neighbor)
            return component
        
        complete_component = 0
        for node in range(n):
            if node not in visited:
                component = helper(node)
                size = len(component)
                if all(len(graph[v]) == size - 1 for v in component):
                    complete_component += 1
        return complete_component