from typing import List


class Solution:
    def isBipartite1(self, graph: List[List[int]]) -> bool:
        n = len(graph)
        color = [-1] * n
        for node in range(n): # handle forrest (graph)
            if color[node] == -1: # if there is a node that is not visited
                stack = [node] # check graph
                while stack:
                    u = stack.pop()
                    for v in graph[u]:
                        if color[v] == -1:
                            stack.append(v)
                            color[v] = 1 - color[u]
                        elif color[u] == color[v]:
                            return False
        return True

    def isBipartite(self, graph: List[List[int]]) -> bool:
        """
        DFS solution
        :param graph:
        :return:
        """
        n = len(graph)
        colors = [-1] * n
        def dfs(color, node): # handle graph
            if colors[node] != -1:
                return colors[node] == color
            colors[node] = color

            for v in graph[node]:
                if not dfs(1 - color, v):
                    return False
            return True

        for node in range(n):
            if colors[node] == -1 and not dfs(1, node): # handle forests
                return False

        return True

if __name__ == "__main__":
    solution = Solution()
    graph = [[1,3],[0,2],[1,3],[0,2]]

    ret = solution.isBipartite(graph)
    print(ret)


