from collections import defaultdict
from typing import List


class Solution:

    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
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