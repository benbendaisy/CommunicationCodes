from typing import List



class GNode(object):
    """  data structure represent a vertex in the graph."""
    def __init__(self):
        self.inDegrees = 0
        self.outNodes = []

class Solution:
    """
    There are a total of numCourses courses you have to take, labeled from 0 to numCourses - 1. You are given an array prerequisites where prerequisites[i] = [ai, bi] indicates that you must take course bi first if you want to take course ai.

    For example, the pair [0, 1], indicates that to take course 0 you have to first take course 1.
    Return true if you can finish all courses. Otherwise, return false.

    Example 1:

    Input: numCourses = 2, prerequisites = [[1,0]]
    Output: true
    Explanation: There are a total of 2 courses to take. 
    To take course 1 you should have finished course 0. So it is possible.
    Example 2:

    Input: numCourses = 2, prerequisites = [[1,0],[0,1]]
    Output: false
    Explanation: There are a total of 2 courses to take. 
    To take course 1 you should have finished course 0, and to take course 0 you should also have finished course 1. So it is impossible.
    """
    def canFinish1(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        from collections import defaultdict, deque
        # key: index of node; value: GNode
        graph = defaultdict(GNode)

        # build the graph
        totalDep = 0
        for dependency in prerequisites:
            cur, dep = dependency[0], dependency[1]
            graph[dep].outNodes.append(cur)
            graph[cur].inDegrees += 1
            totalDep += 1

        # find the node that indegree is zero
        nodepCourses = deque()
        for index, dep in graph.items():
            if dep.inDegrees == 0:
                nodepCourses.append(index)

        removedEdges = 0
        while nodepCourses:
            index = nodepCourses.pop()
            for outIndex in graph[index].outNodes:
                removedEdges += 1
                graph[outIndex].inDegrees -= 1
                if graph[outIndex].inDegrees == 0:
                    nodepCourses.append(outIndex)
        
        return True if removedEdges == totalDep else False
    
    def canFinish2(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        if not prerequisites:
            return True
        
        graph = defaultdict(list)
        in_degree = [0] * numCourses
        for u, v in prerequisites:
            graph[v].append(u)
            in_degree[u] += 1
        que = deque([course for course in range(numCourses) if in_degree[course] == 0])
        cnt = 0
        while que:
            node = que.popleft()
            cnt += 1
            for neighbor in graph[node]:
                in_degree[neighbor] -= 1
                if in_degree[neighbor] == 0:
                    que.append(neighbor)
        return cnt == numCourses