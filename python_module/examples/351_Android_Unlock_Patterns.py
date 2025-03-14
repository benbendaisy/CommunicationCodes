from collections import Counter


class Solution:
    """
        Android devices have a special lock screen with a 3 x 3 grid of dots. Users can set an "unlock pattern" by connecting the dots in a specific sequence, forming a series of joined line segments where each segment's endpoints are two consecutive dots in the sequence. A sequence of k dots is a valid unlock pattern if both of the following are true:

        All the dots in the sequence are distinct.
        If the line segment connecting two consecutive dots in the sequence passes through the center of any other dot, the other dot must have previously appeared in the sequence. No jumps through the center non-selected dots are allowed.
        For example, connecting dots 2 and 9 without dots 5 or 6 appearing beforehand is valid because the line from dot 2 to dot 9 does not pass through the center of either dot 5 or 6.
        However, connecting dots 1 and 3 without dot 2 appearing beforehand is invalid because the line from dot 1 to dot 3 passes through the center of dot 2.
        Here are some example valid and invalid unlock patterns:

        The 1st pattern [4,1,3,6] is invalid because the line connecting dots 1 and 3 pass through dot 2, but dot 2 did not previously appear in the sequence.
        The 2nd pattern [4,1,9,2] is invalid because the line connecting dots 1 and 9 pass through dot 5, but dot 5 did not previously appear in the sequence.
        The 3rd pattern [2,4,1,3,6] is valid because it follows the conditions. The line connecting dots 1 and 3 meets the condition because dot 2 previously appeared in the sequence.
        The 4th pattern [6,5,4,1,9,2] is valid because it follows the conditions. The line connecting dots 1 and 9 meets the condition because dot 5 previously appeared in the sequence.
        Given two integers m and n, return the number of unique and valid unlock patterns of the Android grid lock screen that consist of at least m keys and at most n keys.

        Two unlock patterns are considered unique if there is a dot in one sequence that is not in the other, or the order of the dots is different.

        Example 1:

        Input: m = 1, n = 1
        Output: 9
        Example 2:

        Input: m = 1, n = 2
        Output: 65

        Constraints:

        1 <= m, n <= 9
    """
    def numberOfPatterns1(self, m: int, n: int) -> int:
        """
        # 2 lies between 1 and 3
        # 8 lies between 7 and 9
        # 4 lies between 1 and 7
        # 6 lies between 3 and 9
        # 5 lies between 1, 9    2, 8    3, 7 and 4, 6
        :param m:
        :param n:
        :return:
        """
        dict1 = Counter({(1,3):2,(3,1):2,(1,7):4,(7,1):4,(3,9):6,(9,3):6,(7,9):8,(9,7):8,(1,9):5,(9,1):5,(2,8):5,(8,2):5,(3,7):5,(7,3):5,(4,6):5,(6,4):5})
        visited = [True] + [False]*9

        def backtrack(i, k):
            # if last cell then return 1 way
            if not k:
                return 1

            total = 0

            # make this cell visited before
            # going to next call
            visited[i] = True
            for j in range(1,10):
                '''
                    * if this cell is not visit AND either i and j are adjacent (then
                    * jump[i][j] = 0) or between cell must be visit already ( then
                    * visit[jump[i][j]] = 1)
                '''
                if not visited[j] and visited[dict1[(i, j)]]:
                    total += backtrack(j, k-1)

            # make this cell not visited
            # after returning from call
            visited[i] = False
            return total
            # 1, 3, 7, 9 are symmetric so multiplying by 4
            # 2, 4, 6, 8 are symmetric so multiplying by 4
        return sum(backtrack(1, k) * 4 + backtrack(2, k) * 4 + backtrack(5, k) for k in range(m - 1, n))
    
    def numberOfPatterns2(self, m: int, n: int) -> int:
        # Define the skip conditions
        skip = [[0] * 10 for _ in range(10)]
        skip[1][3] = skip[3][1] = 2
        skip[1][7] = skip[7][1] = 4
        skip[3][9] = skip[9][3] = 6
        skip[7][9] = skip[9][7] = 8
        skip[1][9] = skip[9][1] = skip[3][7] = skip[7][3] = skip[2][8] = skip[8][2] = skip[4][6] = skip[6][4] = 5

        # Visited array to keep track of visited dots
        visited = [False] * 10

        # Recursive function to count valid patterns
        def backtrack(current, remaining):
            if remaining < 0:
                return 0
            if remaining == 0:
                return 1
            visited[current] = True
            count = 0
            for next_dot in range(1, 10):
                if not visited[next_dot]:
                    # Check if the move is valid
                    if skip[current][next_dot] == 0 or visited[skip[current][next_dot]]:
                        count += backtrack(next_dot, remaining - 1)
            visited[current] = False
            return count

        # Calculate the total number of patterns
        total = 0
        for length in range(m, n + 1):
            for start in range(1, 10):
                total += backtrack(start, length - 1)
        return total
    
    def numberOfPatterns3(self, m: int, n: int) -> int:
        skip = {
            (1, 3): 2, (3, 1): 2, (1, 7): 4, (7, 1): 4,
            (3, 9): 6, (9, 3): 6, (7, 9): 8, (9, 7): 8,
            (1, 9): 5, (9, 1): 5, (3, 7): 5, (7, 3): 5,
            (2, 8): 5, (8, 2): 5, (4, 6): 5, (6, 4): 5
        }
        
        @cache
        def helper(curr: int, remaining: int, mask: int) -> int:
            if remaining == 0:
                return 1
            cnt = 0
            for nxt in range(1, 10):
                if (mask & (1 << nxt)) == 0 and (
                    (curr, nxt) not in skip or (mask & (1 << skip[(curr, nxt)])) != 0
                ):
                    cnt += helper(nxt, remaining - 1, mask | (1 << nxt))
            return cnt
        
        res = 0
        for length in range(m, n + 1):
            for start in range(1, 10):
                res += helper(start, length - 1, 1 << start)
        
        return res
    
    def numberOfPatterns(self, m: int, n: int) -> int:
        skip = {}
        skip[(1, 3)] = skip[(3, 1)] = 2
        skip[(1, 7)] = skip[(7, 1)] = 4
        skip[(3, 9)] = skip[(9, 3)] = 6
        skip[(7, 9)] = skip[(9, 7)] = 8
        skip[(1, 9)] = skip[(9, 1)] = skip[(3, 7)] = skip[(7, 3)] = skip[(2, 8)] = skip[(8, 2)] = skip[(4, 6)] = skip[(6, 4)] = 5
        @cache
        def helper(curr: int, remaining: int, mask: int):
            if remaining == 0:
                return 1
            cnt = 0
            for nxt in range(1, 10):
                if (mask & (1 << nxt)) == 0 and (
                    (curr, nxt) not in skip or (mask & (1 << skip[(curr, nxt)])) != 0
                ):
                        new_mask = mask | (1 << nxt)
                        cnt += helper(nxt, remaining - 1, new_mask)
            return cnt
        res = 0
        for length in range(m, n + 1):
            for start in range(1, 10):
                res += helper(start, length - 1, 1 << start)
        return res