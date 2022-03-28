from typing import List

class GraphNode:
    def __init__(self):
        self.inDegree = 0
        self.outNodes = []

class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        if not prerequisites:
            return []
        elif numCourses == 1:
            return [0]
        from collections import defaultdict, deque
        graph = defaultdict(GraphNode)

        for dependency in prerequisites:
            cur, dep = dependency
            graph[cur].inDegree += 1
            graph[dep].outNodes.append(cur)

        # find the nodes whose degree is zero
        que = deque()
        for idx in range(numCourses):
            if graph[idx].inDegree == 0:
                que.append(idx)

        # sort the output
        res = []
        while que:
            idx = que.pop()
            res.append(idx)
            for outIdx in graph[idx].outNodes:
                graph[outIdx].inDegree -= 1
                if graph[outIdx].inDegree == 0:
                    que.append(outIdx)

        return res if len(res) == numCourses else []
