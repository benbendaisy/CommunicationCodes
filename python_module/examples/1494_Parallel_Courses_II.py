class Solution:
    """
    You are given an integer n, which indicates that there are n courses labeled from 1 to n. You are also given an array relations where relations[i] = [prevCoursei, nextCoursei], representing a prerequisite relationship between course prevCoursei and course nextCoursei: course prevCoursei has to be taken before course nextCoursei. Also, you are given the integer k.

    In one semester, you can take at most k courses as long as you have taken all the prerequisites in the previous semesters for the courses you are taking.

    Return the minimum number of semesters needed to take all courses. The testcases will be generated such that it is possible to take every course.

    Example 1:

    Input: n = 4, relations = [[2,1],[3,1],[1,4]], k = 2
    Output: 3
    Explanation: The figure above represents the given graph.
    In the first semester, you can take courses 2 and 3.
    In the second semester, you can take course 1.
    In the third semester, you can take course 4.
    Example 2:

    Input: n = 5, relations = [[2,1],[3,1],[4,1],[1,5]], k = 2
    Output: 4
    Explanation: The figure above represents the given graph.
    In the first semester, you can only take courses 2 and 3 since you cannot take more than two per semester.
    In the second semester, you can take course 4.
    In the third semester, you can take course 1.
    In the fourth semester, you can take course 5.
    """
    def minNumberOfSemesters1(self, n: int, relations: List[List[int]], k: int) -> int:
        """
        Find the minimum number of semesters needed to take all courses.
        
        Args:
            n: Number of courses labeled from 1 to n
            relations: List of [prevCourse, nextCourse] pairs
            k: Maximum number of courses you can take in one semester
        
        Returns:
            Minimum number of semesters needed
        
        Note: it is not working for some corner cases
        """
        # Build adjacency list and calculate in-degree for each course
        graph = defaultdict(list)
        in_degree = [0] * (n + 1)  # +1 because courses are labeled from 1 to n
        
        for prev, next in relations:
            graph[prev].append(next)
            in_degree[next] += 1
        
        # Queue for courses with no prerequisites (in-degree = 0)
        queue = deque()
        for i in range(1, n + 1):
            if in_degree[i] == 0:
                queue.append(i)
        
        semesters = 0
        courses_taken = 0
        
        # Process courses semester by semester
        while queue:
            semester_size = min(len(queue), k)  # Take at most k courses this semester
            
            # Process all courses for this semester
            for _ in range(semester_size):
                course = queue.popleft()
                courses_taken += 1
                
                # Update in-degree for all dependent courses
                for next_course in graph[course]:
                    in_degree[next_course] -= 1
                    if in_degree[next_course] == 0:
                        queue.append(next_course)
            
            semesters += 1
        
        # If we couldn't take all courses, there's a cycle in the graph
        return semesters if courses_taken == n else -1
    
    def minNumberOfSemesters2(self, n: int, relations: List[List[int]], k: int) -> int:
        """
        try all combinations
        """
        f = defaultdict(list)
        for x, y in relations:
            f[y].append(x)

        cands = [x for x in range(1, n+1) if x not in f]
        stack = [(1, list(x)) for x in combinations(cands, min(k, len(cands)))]
        vis = set()
        while stack:
            semester, taken = heappop(stack)
            if len(taken) == n:
                return semester
            cands = [x for x in range(1, n+1) if x not in taken and all(y in taken for y in f[x])]
            for cand in combinations(cands, min(k, len(cands))):
                newtaken = sorted(taken+list(cand))
                if (tuple(newtaken), semester+1) not in vis:
                    vis.add((tuple(newtaken), semester+1))
                    heappush(stack, (semester+1, newtaken))
    
    def minNumberOfSemesters3(self, n: int, relations: List[List[int]], k: int) -> int:
        freq = defaultdict(list)
        for x, y in relations:
            freq[y].append(x)

        cands = [x for x in range(1, n + 1) if x not in freq]
        stack = [(1, list(x)) for x in combinations(cands, min(k, len(cands)))]
        vis = set()
        while stack:
            semester, taken = heappop(stack)
            if len(taken) == n:
                return semester
            cands = [x for x in range(1, n + 1) if x not in taken and all(y in taken for y in freq[x])]
            for cand in combinations(cands, min(k, len(cands))):
                new_taken = sorted(taken + list(cand))
                if (semester + 1, tuple(new_taken)) not in vis:
                    vis.add((semester + 1, tuple(new_taken)))
                    heappush(stack, (semester + 1, new_taken))