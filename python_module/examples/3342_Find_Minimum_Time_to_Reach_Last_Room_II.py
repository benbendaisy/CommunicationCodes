class Solution:
    """
    here is a dungeon with n x m rooms arranged as a grid.

    You are given a 2D array moveTime of size n x m, where moveTime[i][j] represents the minimum time in seconds when you can start moving to that room. You start from the room (0, 0) at time t = 0 and can move to an adjacent room. Moving between adjacent rooms takes one second for one move and two seconds for the next, alternating between the two.

    Return the minimum time to reach the room (n - 1, m - 1).

    Two rooms are adjacent if they share a common wall, either horizontally or vertically.

    Example 1:

    Input: moveTime = [[0,4],[4,4]]

    Output: 7

    Explanation:

    The minimum time required is 7 seconds.

    At time t == 4, move from room (0, 0) to room (1, 0) in one second.
    At time t == 5, move from room (1, 0) to room (1, 1) in two seconds.
    Example 2:

    Input: moveTime = [[0,0,0,0],[0,0,0,0]]

    Output: 6

    Explanation:

    The minimum time required is 6 seconds.

    At time t == 0, move from room (0, 0) to room (1, 0) in one second.
    At time t == 1, move from room (1, 0) to room (1, 1) in two seconds.
    At time t == 3, move from room (1, 1) to room (1, 2) in one second.
    At time t == 4, move from room (1, 2) to room (1, 3) in two seconds.
    Example 3:

    Input: moveTime = [[0,1],[1,2]]

    Output: 4
    """
    def minTimeToReach(self, moveTime: List[List[int]]) -> int:
        if not moveTime:
            return 0
        m, n = len(moveTime), len(moveTime[0])
        dist = [[float('inf')] * n for _ in range(m)]
        visited = set()
        dirs = ((1, 0), (-1, 0), (0, -1), (0, 1))

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
                if not (0 <= nx < m and 0 <= ny < n):
                    continue
                d = max(dist[x][y], moveTime[nx][ny]) + (x + y) % 2 + 1
                if dist[nx][ny] > d:
                    dist[nx][ny] = d
                    heapq.heappush(que, (d, nx, ny))
        return dist[m - 1][n - 1]