class Solution:
    """
    There is a dungeon with n x m rooms arranged as a grid.

    You are given a 2D array moveTime of size n x m, where moveTime[i][j] represents the minimum time in seconds when you can start moving to that room. You start from the room (0, 0) at time t = 0 and can move to an adjacent room. Moving between adjacent rooms takes exactly one second.

    Return the minimum time to reach the room (n - 1, m - 1).

    Two rooms are adjacent if they share a common wall, either horizontally or vertically.

    Example 1:

    Input: moveTime = [[0,4],[4,4]]

    Output: 6

    Explanation:

    The minimum time required is 6 seconds.

    At time t == 4, move from room (0, 0) to room (1, 0) in one second.
    At time t == 5, move from room (1, 0) to room (1, 1) in one second.
    Example 2:

    Input: moveTime = [[0,0,0],[0,0,0]]

    Output: 3

    Explanation:

    The minimum time required is 3 seconds.

    At time t == 0, move from room (0, 0) to room (1, 0) in one second.
    At time t == 1, move from room (1, 0) to room (1, 1) in one second.
    At time t == 2, move from room (1, 1) to room (1, 2) in one second.
    Example 3:

    Input: moveTime = [[0,1],[1,2]]

    Output: 3
    """
    class State:
        def __init__(self, x, y, dis):
            self.x = x
            self.y = y
            self.dis = dis

        def __lt__(self, other):
            return self.dis < other.dis
    def minTimeToReach1(self, moveTime: List[List[int]]) -> int:
        n = len(moveTime)
        m = len(moveTime[0])
        inf = float("inf")
        d = [[inf] * m for _ in range(n)]
        v = [[0] * m for _ in range(n)]

        dirs = [(1, 0), (-1, 0), (0, 1), (0, -1)]

        d[0][0] = 0
        q = []
        heapq.heappush(q, State(0, 0, 0))

        while q:
            s = heapq.heappop(q)
            if v[s.x][s.y]:
                continue
            v[s.x][s.y] = 1
            for dx, dy in dirs:
                nx, ny = s.x + dx, s.y + dy
                if not (0 <= nx < n and 0 <= ny < m):
                    continue
                dist = max(d[s.x][s.y], moveTime[nx][ny]) + 1
                if d[nx][ny] > dist:
                    d[nx][ny] = dist
                    heapq.heappush(q, State(nx, ny, dist))

        return d[n - 1][m - 1]
    
    def minTimeToReach2(self, moveTime: List[List[int]]) -> int:
        n = len(moveTime)
        m = len(moveTime[0])
        inf = float("inf")
        dist = [[inf] * m for _ in range(n)]
        visited = set()
        dirs = [(1, 0), (-1, 0), (0, 1), (0, -1)]

        dist[0][0] = 0
        q = []
        heapq.heappush(q, State(0, 0, 0))

        while q:
            s = heapq.heappop(q)
            if (s.x, s.y) in visited:
                continue
            visited.add((s.x, s.y))
            for dx, dy in dirs:
                nx, ny = s.x + dx, s.y + dy
                if not (0 <= nx < n and 0 <= ny < m):
                    continue
                d = max(dist[s.x][s.y], moveTime[nx][ny]) + 1
                if dist[nx][ny] > d:
                    dist[nx][ny] = d
                    heapq.heappush(q, State(nx, ny, d))

        return dist[n - 1][m - 1]
    
    def minTimeToReach(self, moveTime: List[List[int]]) -> int:
        n, m = len(moveTime), len(moveTime[0])
        inf = float("inf")
        dist = [[inf] * m for _ in range(n)]
        visited = set()
        dirs = [(1, 0), (-1, 0), (0, 1), (0, -1)]

        dist[0][0] = 0
        que = []
        heapq.heappush(que, (0, 0, 0))

        while que:
            _, x, y = heapq.heappop(que)
            if (x, y) in visited:
                continue
            visited.add((x, y))
            for dx, dy in dirs:
                nx, ny = x + dx, y + dy
                if not (0 <= nx < n and 0 <= ny < m):
                    continue
                d = max(dist[x][y], moveTime[nx][ny]) + 1
                if dist[nx][ny] > d:
                    dist[nx][ny] = d
                    heapq.heappush(que, (d, nx, ny))

        return dist[n - 1][m - 1]