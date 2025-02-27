from typing import List


class Solution:
    """
        You are given an integer array arr. From some starting index, you can make a series of jumps. The (1st, 3rd, 5th, ...) jumps in the series are called odd-numbered jumps, and the (2nd, 4th, 6th, ...) jumps in the series are called even-numbered jumps. Note that the jumps are numbered, not the indices.

        You may jump forward from index i to index j (with i < j) in the following way:

        During odd-numbered jumps (i.e., jumps 1, 3, 5, ...), you jump to the index j such that arr[i] <= arr[j] and arr[j] is the smallest possible value. If there are multiple such indices j, you can only jump to the smallest such index j.
        During even-numbered jumps (i.e., jumps 2, 4, 6, ...), you jump to the index j such that arr[i] >= arr[j] and arr[j] is the largest possible value. If there are multiple such indices j, you can only jump to the smallest such index j.
        It may be the case that for some index i, there are no legal jumps.
        A starting index is good if, starting from that index, you can reach the end of the array (index arr.length - 1) by jumping some number of times (possibly 0 or more than once).

        Return the number of good starting indices.

        Example 1:

        Input: arr = [10,13,12,14,15]
        Output: 2
        Explanation:
        From starting index i = 0, we can make our 1st jump to i = 2 (since arr[2] is the smallest among arr[1], arr[2], arr[3], arr[4] that is greater or equal to arr[0]), then we cannot jump any more.
        From starting index i = 1 and i = 2, we can make our 1st jump to i = 3, then we cannot jump any more.
        From starting index i = 3, we can make our 1st jump to i = 4, so we have reached the end.
        From starting index i = 4, we have reached the end already.
        In total, there are 2 different starting indices i = 3 and i = 4, where we can reach the end with some number of
        jumps.
        Example 2:

        Input: arr = [2,3,1,1,4]
        Output: 3
        Explanation:
        From starting index i = 0, we make jumps to i = 1, i = 2, i = 3:
        During our 1st jump (odd-numbered), we first jump to i = 1 because arr[1] is the smallest value in [arr[1], arr[2], arr[3], arr[4]] that is greater than or equal to arr[0].
        During our 2nd jump (even-numbered), we jump from i = 1 to i = 2 because arr[2] is the largest value in [arr[2], arr[3], arr[4]] that is less than or equal to arr[1]. arr[3] is also the largest value, but 2 is a smaller index, so we can only jump to i = 2 and not i = 3
        During our 3rd jump (odd-numbered), we jump from i = 2 to i = 3 because arr[3] is the smallest value in [arr[3], arr[4]] that is greater than or equal to arr[2].
        We can't jump from i = 3 to i = 4, so the starting index i = 0 is not good.
        In a similar manner, we can deduce that:
        From starting index i = 1, we jump to i = 4, so we reach the end.
        From starting index i = 2, we jump to i = 3, and then we can't jump anymore.
        From starting index i = 3, we jump to i = 4, so we reach the end.
        From starting index i = 4, we are already at the end.
        In total, there are 3 different starting indices i = 1, i = 3, and i = 4, where we can reach the end with some
        number of jumps.
        Example 3:

        Input: arr = [5,1,3,4,2]
        Output: 3
        Explanation: We can reach the end from starting indices 1, 2, and 4.
    """
    def oddEvenJumps1(self, arr: List[int]) -> int:
        # find next index of current index that is the least larger/smaller
        def get_next_index(sorted_indexes):
            stack = []
            n = len(sorted_indexes)
            res = [None] * n
            for idx in sorted_indexes:
                while stack and idx > stack[-1]:
                    res[stack.pop()] = idx
                stack.append(idx)
            return res

        sorted_indexes = sorted(range(len(arr)), key=lambda x: arr[x])
        odd_indexes = get_next_index(sorted_indexes)
        sorted_indexes.sort(key=lambda x: -arr[x])
        even_indexes = get_next_index(sorted_indexes)

        # [odd, even], the 0th jump is even
        dp = [[0, 1] for _ in range(len(arr))]

        for i in range(len(arr)):
            if odd_indexes[i] is not None:
                dp[odd_indexes[i]][0] += dp[i][1]
            if even_indexes[i] is not None:
                dp[even_indexes[i]][1] += dp[i][0]
        return dp[-1][0] + dp[-1][1]
    

    def oddEvenJumps2(arr):
        n = len(arr)
        if n == 1:
            return 1  # Only one element, always valid

        # Step 1: Precompute next jumps using monotonic stacks
        def next_jump(order):
            result = [None] * n
            stack = []
            for i in order:
                while stack and stack[-1] < i:
                    result[stack.pop()] = i
                stack.append(i)
            return result

        odd_jump = next_jump(sorted(range(n), key=lambda i: (arr[i], i)))  # Increasing order
        even_jump = next_jump(sorted(range(n), key=lambda i: (-arr[i], i)))  # Decreasing order

        # Step 2: Dynamic Programming
        odd = [False] * n
        even = [False] * n
        odd[-1] = even[-1] = True  # The last index is always valid

        for i in range(n - 2, -1, -1):
            if odd_jump[i] is not None:
                odd[i] = even[odd_jump[i]]
            if even_jump[i] is not None:
                even[i] = odd[even_jump[i]]

        return sum(odd)  # Count good starting indices
    
    def oddEvenJumps(arr):
        n = len(arr)

        # Helper function to find the next jump index
        def next_jump(odd):
            result = [None] * n
            stack = []
            for i in sorted(range(n), key=lambda x: (arr[x], x) if odd else (-arr[x], x)):
                while stack and stack[-1] < i:
                    result[stack.pop()] = i
                stack.append(i)
            return result

        # Precompute next jumps using monotonic stacks
        odd_jump = next_jump(odd=True)
        even_jump = next_jump(odd=False)

        @lru_cache(None)  # Memoization to store computed results
        def dfs(i, odd_turn):
            if i == n - 1:
                return True  # Reached the last index

            next_index = odd_jump[i] if odd_turn else even_jump[i]
            if next_index is None:
                return False  # No valid jump
            
            return dfs(next_index, not odd_turn)

        # Count good starting indices
        return sum(dfs(i, True) for i in range(n))