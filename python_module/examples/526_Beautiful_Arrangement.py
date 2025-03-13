class Solution:
    """
    Suppose you have n integers labeled 1 through n. A permutation of those n integers perm (1-indexed) is considered a beautiful arrangement if for every i (1 <= i <= n), either of the following is true:

    perm[i] is divisible by i.
    i is divisible by perm[i].
    Given an integer n, return the number of the beautiful arrangements that you can construct.

    Example 1:

    Input: n = 2
    Output: 2
    Explanation: 
    The first beautiful arrangement is [1,2]:
        - perm[1] = 1 is divisible by i = 1
        - perm[2] = 2 is divisible by i = 2
    The second beautiful arrangement is [2,1]:
        - perm[1] = 2 is divisible by i = 1
        - i = 2 is divisible by perm[2] = 1
    Example 2:

    Input: n = 1
    Output: 1
    """
    def countArrangement1(self, n: int) -> int:
        def backtrack(index):
            if index > n:
                return 1  # Found a valid arrangement
            
            count = 0
            for num in range(1, n + 1):
                if not visited[num] and (num % index == 0 or index % num == 0):
                    visited[num] = True  # Mark as used
                    count += backtrack(index + 1)
                    visited[num] = False  # Backtrack
            
            return count
        
        visited = [False] * (n + 1)
        return backtrack(1)
    
    def countArrangement2(self, n: int) -> int:
        visited = [False] * (n + 1)

        def helper(idx: int):
            if idx > n:
                return 1
            
            cnt = 0
            for num in range(1, n + 1):
                if not visited[num] and (num % idx == 0 or idx % num == 0):
                    visited[num] = True
                    cnt += helper(idx + 1)
                    visited[num] = False
            return cnt
        return helper(1)
    
    def countArrangement(self, n: int) -> int:
        @cache
        def helper(idx: int, mask: int) -> int:
            if idx == n + 1:
                return 1
            
            ways = 0
            for i in range(1, n + 1):
                if (mask & 1 << i) == 0 and (i % idx == 0 or idx % i == 0):
                    new_mask = mask | 1 << i
                    ways += helper(idx + 1, new_mask)
            return ways
        
        return helper(1, 0)