class Solution:
    """
    You are given an m x n integer matrix grid and an array queries of size k.

    Find an array answer of size k such that for each integer queries[i] you start in the top left cell of the matrix and repeat the following process:

    If queries[i] is strictly greater than the value of the current cell that you are in, then you get one point if it is your first time visiting this cell, and you can move to any adjacent cell in all 4 directions: up, down, left, and right.
    Otherwise, you do not get any points, and you end this process.
    After the process, answer[i] is the maximum number of points you can get. Note that for each query you are allowed to visit the same cell multiple times.

    Return the resulting array answer.

    Example 1:

    Input: grid = [[1,2,3],[2,5,7],[3,5,1]], queries = [5,6,2]
    Output: [5,8,1]
    Explanation: The diagrams above show which cells we visit to get points for each query.
    Example 2:

    Input: grid = [[5,2,1],[1,1,2]], queries = [3]
    Output: [0]
    Explanation: We can not get any points because the value of the top left cell is already greater than or equal to 3.
    """
    def maxPoints1(self, grid: List[List[int]], queries: List[int]) -> List[int]:
        """
        Time Limit Exceeded
        """
        m, n = len(grid), len(grid[0])
        def helper(row: int, col: int, target: int) -> int:
            if grid[row][col] > target:
                return 0
            que = deque([(row, col)])
            visited = set([(row, col)])
            cnt = 0
            while que:
                r, c = que.popleft()
                cnt += 1
                for dx, dy in ((-1, 0), (1, 0), (0, -1), (0, 1)):
                    new_r, new_c = r + dx, c + dy
                    if 0 <= new_r < m and 0 <= new_c < n and grid[new_r][new_c] < target and (new_r, new_c) not in visited:
                        que.append((new_r, new_c))
                        visited.add((new_r, new_c))
            return cnt
        ans = []
        for q in queries:
            cnt = helper(0, 0, q)
            ans.append(cnt)
        return ans
    
    def maxPoints(self, grid: List[List[int]], queries: List[int]) -> List[int]:
        m, n = len(grid), len(grid[0])
        queries_sorted = sorted(enumerate(queries), key=lambda x: x[1])  # Sort queries with original indices
        ans = [0] * len(queries)

        min_heap = [(grid[0][0], 0, 0)]  # Min-heap (cell value, row, col)
        visited = set([(0, 0)])
        count = 0  # Track accessible cells

        for i, q in queries_sorted:
            while min_heap and min_heap[0][0] < q:
                _, r, c = heappop(min_heap)
                count += 1  # This cell is now reachable
                
                # Explore adjacent cells
                for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                    new_r, new_c = r + dx, c + dy
                    if 0 <= new_r < m and 0 <= new_c < n and (new_r, new_c) not in visited:
                        heappush(min_heap, (grid[new_r][new_c], new_r, new_c))
                        visited.add((new_r, new_c))
            
            ans[i] = count  # Store result in original query order

        return ans