import heapq
import queue
from functools import lru_cache
from typing import List


class Solution:
    """
        There are n different online courses numbered from 1 to n. You are given an array courses where courses[i] = [durationi, lastDayi] indicate that the ith course should be taken continuously for durationi days and must be finished before or on lastDayi.

        You will start on the 1st day and you cannot take two or more courses simultaneously.

        Return the maximum number of courses that you can take.

        Example 1:

        Input: courses = [[100,200],[200,1300],[1000,1250],[2000,3200]]
        Output: 3
        Explanation:
        There are totally 4 courses, but you can take 3 courses at most:
        First, take the 1st course, it costs 100 days so you will finish it on the 100th day, and ready to take the next course on the 101st day.
        Second, take the 3rd course, it costs 1000 days so you will finish it on the 1100th day, and ready to take the next course on the 1101st day.
        Third, take the 2nd course, it costs 200 days so you will finish it on the 1300th day.
        The 4th course cannot be taken now, since you will finish it on the 3300th day, which exceeds the closed date.
        Example 2:

        Input: courses = [[1,2]]
        Output: 1
        Example 3:

        Input: courses = [[3,2],[4,3]]
        Output: 0

        Constraints:

        1 <= courses.length <= 104
        1 <= durationi, lastDayi <= 104
    """
    def scheduleCourse(self, courses: List[List[int]]) -> int:
        if not courses:
            return 0
        courses.sort(key=lambda x: x[1])
        memory = [[0] * sum([courses[i][0] for i in range(len(courses))])] * len(courses)

        def scheduleCourses(courses: List[List[int]], memory: List[List[int]], i: int, time: int):
            if i == len(courses):
                return 0
            elif memory[i][time]:
                return memory[i][time]
            taken = 0
            if time + courses[i][0] <= courses[i][1]:
                taken = 1 + scheduleCourses(courses, memory, i + 1, time + courses[i][0])
            not_taken = scheduleCourses(courses, memory, i + 1, time)
            memory[i][time] = max(taken, not_taken)
            return memory[i][time]

        return scheduleCourses(courses, memory, 0, 0)

    def scheduleCourse1(self, courses: List[List[int]]) -> int:
        if not courses:
            return -1

        courses.sort(key=lambda x: x[1])
        time = cnt = 0
        for i in range(len(courses)):
            if time + courses[i][0] <= courses[i][1]:
                time += courses[i][0]
                cnt += 1
            else:
                max_index = i
                for j in range(i):
                    if courses[j][0] > courses[max_index][0]:
                        max_index = j

                if courses[max_index][0] > courses[i][0]:
                    time += courses[i][0] - courses[max_index][0]
                courses[max_index][0] = -1
        return cnt

    def scheduleCourse2(self, courses: List[List[int]]) -> int:
        courses.sort(key= lambda x: x[1])
        @lru_cache(None)
        def scheduleCourses(i: int, time: int):
            if i == len(courses):
                return 0
            taken = 0
            if time + courses[i][0] <=courses[i][1]:
                taken = 1 + scheduleCourses(i + 1, time + courses[i][0])
            notTaken = scheduleCourses(i + 1, time)
            return max(taken, notTaken)
        return scheduleCourses(0, 0)

    def scheduleCourse(self, courses: List[List[int]]) -> int:
        courses.sort(key=lambda x: x[1])
        arr, time = [], 0
        for course in courses:
            heapq.heappush(arr, -course[0])
            time += course[0]
            while time > course[1]:
                time += heapq.heappop(arr)
        return len(arr)

if __name__ == "__main__":
    solution = Solution()
    courses = [[7,16],[2,3],[3,12],[3,14],[10,19],[10,16],[6,8],[6,11],[3,13],[6,16]]
    ret = solution.scheduleCourse(courses)
    print(ret)