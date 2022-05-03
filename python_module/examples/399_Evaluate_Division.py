import collections
from collections import defaultdict
from typing import List


class Solution:
    def calcEquation1(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        graph = defaultdict(defaultdict)

        def backtrack_evaluate(source, target, product, visited):
            visited.add(source)
            ret = -1.0
            neighbors = graph[source]
            if target in neighbors:
                ret = product * graph[source][target]
            else:
                for neighbor, value in neighbors.items():
                    if neighbor in visited:
                        continue
                    ret = backtrack_evaluate(neighbor, target, product * value, visited)
                    if ret != -1.0:
                        break
            visited.remove(source)
            return ret

        for (dividend, divisor), value in zip(equations, values):
            graph[dividend][divisor] = value
            graph[divisor][dividend] = 1 / value

        res = []
        for dividend, divisor in queries:
            if dividend not in graph or divisor not in graph:
                ret = -1.0
            elif dividend == divisor:
                ret = 1.0
            else:
                visited = set()
                ret = backtrack_evaluate(dividend, divisor, 1.0, visited)
            res.append(ret)
        return res

    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        graph = collections.defaultdict(dict)
        for (source, target), value in zip(equations, values):
            graph[source][target] = value
            graph[target][source] = 1 / value

        def bfs(source, target):
            if source not in graph or target not in graph:
                return -1.0

            q, visited = [(source, 1.0)], set()
            for x, v in q:
                if x == target:
                    return v
                visited.add(x)
                for y in graph[x]:
                    if y not in visited:
                        q.append((y, v * graph[x][y]))
            return -1.0

        return [bfs(source, target) for source, target in queries]
