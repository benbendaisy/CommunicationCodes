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

    def calcEquation2(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
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
    
    def calcEquation3(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        if not equations:
            return []
        
        # Build the graph
        graph = defaultdict(list)
        for (a, b), val in zip(equations, values):
            graph[a].append((b, val))
            graph[b].append((a, 1.0 / val))

        def helper(source: str, target: str, running_score: float) -> float:
            if source not in graph or target not in graph:
                return -1.0  # If either variable doesn't exist in the graph
            
            if source == target:
                return running_score

            visited.add(source)

            for neighbor, score in graph[source]:
                if neighbor not in visited:
                    result = helper(neighbor, target, running_score * score)
                    if result != -1.0:
                        return result

            return -1.0  # No valid path found

        # Process queries
        res = []
        for query in queries:
            src, dst = query
            visited = set()
            if src not in graph or dst not in graph:
                res.append(-1.0)
            else:
                res.append(helper(src, dst, 1.0))
        
        return res
    
    def calcEquation4(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        if not equations:
            return []
        graph = defaultdict(list)
        for i, value in enumerate(equations):
            graph[value[0]].append((value[1], values[i]))
            graph[value[1]].append((value[0], 1.0 / values[i]))
        
        def helper(source: str, target: str, running_score: float):
            if source not in graph or target not in graph:
                return -1.0

            if source == target:
                return running_score
            
            visited.add(source)

            for neighbor, score in graph[source]:
                if neighbor not in visited:
                    t = helper(neighbor, target, running_score * score)
                    if t != -1.0:
                        return t
                    visited.remove(neighbor)

            return -1.0
        
        res = []
        for query in queries:
            visited = set()
            res.append(helper(query[0], query[1], 1.0))
        return res
