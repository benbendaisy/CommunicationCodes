from collections import defaultdict
from typing import List

class GNode(object):
    """  data structure represent a vertex in the graph."""
    def __init__(self):
        self.inDegrees = 0
        self.outNodes = []

class Solution:
    def canFinish(self, numCourses, prerequisites):
        """
        :type numCourses: int
        :type prerequisites: List[List[int]]
        :rtype: bool
        """
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



    def canFinish1(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        if numCourses <= 1:
            return True

        dep_map = defaultdict(list)
        for preList in prerequisites:
            a, b = preList[0], preList[1]
            dep_map[a].append(b)

        path = [False] * numCourses
        checked = [False] * numCourses
        for i in range(numCourses):
            if self.isCyclic(i, dep_map, checked, path):
                return False

        return True

    def isCyclic(self, currCourse, courseDict, checked, path):
        if checked[currCourse]:
            return False
        if path[currCourse]:
            return True

        path[currCourse] = True
        ret = False
        for dependCourse in courseDict[currCourse]:
            ret = self.isCyclic(dependCourse, courseDict, checked, path)
            if ret: break

        path[currCourse] = False

        checked[currCourse] = True
        return ret