from typing import List


class Solution:
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

if __name__ == "__main__":
    solution = Solution()
    courses = [[7,16],[2,3],[3,12],[3,14],[10,19],[10,16],[6,8],[6,11],[3,13],[6,16]]
    ret = solution.scheduleCourse(courses)
    print(ret)