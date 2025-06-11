class Solution:
    """
        Given two integers n and k, return the kth lexicographically smallest integer in the range [1, n].

        Example 1:

        Input: n = 13, k = 2
        Output: 10
        Explanation: The lexicographical order is [1, 10, 11, 12, 13, 2, 3, 4, 5, 6, 7, 8, 9], so the second smallest number is 10.
        Example 2:

        Input: n = 1, k = 1
        Output: 1
    """
    def findKthNumber1(self, n: int, k: int) -> int:
        def get_steps(n1, n2):
            steps = 0
            while n1 <= n:
                steps += min(n + 1, n2) - n1
                n1 *= 10
                n2 *= 10
            return steps
        if k == 1:
            return 1
        k -= 1
        cur = 1
        while k > 0:
            steps = get_steps(cur, cur + 1)
            if steps <= k:
                cur += 1
                k -= steps
            else:
                cur *= 10
                k -= 1
        return cur

    def findKthNumber2(self, n: int, k: int) -> int:
        def fn(x):
            ans, diff = 0, 1
            while x <= n:
                ans += min(n - x + 1, diff)
                x *= 10
                diff *= 10
            return ans

        x = 1
        while k > 1:
            cnt = fn(x)
            if k > cnt:
                k -= cnt
                x += 1
            else:
                k -= 1
                x *= 10
        return x
    
    def findKthNumber3(self, n: int, k: int) -> int:
        """
        Finds the k-th lexicographically smallest integer in the range [1, n].

        Args:
        n: The upper bound of the range (inclusive).
        k: The k-th smallest number to find.

        Returns:
        The k-th lexicographically smallest integer.
        """

        def get_steps(curr: int, n: int) -> int:
            """
            Calculates the number of integers in the lexicographical tree that are
            prefixed by `curr`.
            """
            steps = 0
            first = curr
            last = curr
            while first <= n:
                steps += min(n, last) - first + 1
                first *= 10
                last = last * 10 + 9
            return steps

        curr = 1
        k -= 1  # Adjust k to be 0-indexed

        while k > 0:
            steps = get_steps(curr, n)

            if steps <= k:
                k -= steps
                curr += 1
            else:
                k -= 1
                curr *= 10

        return curr
    
    def findKthNumber4(self, n, k):
        # To count how many numbers exist between prefix1 and prefix2
        def helper(prefix1, prefix2):
            steps = 0
            while prefix1 <= n:
                steps += min(n + 1, prefix2) - prefix1
                prefix1 *= 10
                prefix2 *= 10
            return steps
        
        curr = 1
        k -= 1

        while k > 0:
            step = helper(curr, curr + 1)
            # If the steps are less than or equal to k, we skip this prefix's subtree
            if step <= k:
                # Move to the next prefix and decrease k by the number of steps we skip
                curr += 1
                k -= step
            else:
                # Move to the next level of the tree and decrement k by 1
                curr *= 10
                k -= 1

        return curr

    