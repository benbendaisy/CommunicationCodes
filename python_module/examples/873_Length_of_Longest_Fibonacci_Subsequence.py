class Solution:
    """
    A sequence x1, x2, ..., xn is Fibonacci-like if:

    n >= 3
    xi + xi+1 == xi+2 for all i + 2 <= n
    Given a strictly increasing array arr of positive integers forming a sequence, return the length of the longest Fibonacci-like subsequence of arr. If one does not exist, return 0.

    A subsequence is derived from another sequence arr by deleting any number of elements (including none) from arr, without changing the order of the remaining elements. For example, [3, 5, 8] is a subsequence of [3, 4, 5, 6, 7, 8].

    Example 1:

    Input: arr = [1,2,3,4,5,6,7,8]
    Output: 5
    Explanation: The longest subsequence that is fibonacci-like: [1,2,3,5,8].
    Example 2:

    Input: arr = [1,3,7,11,12,14,18]
    Output: 3
    Explanation: The longest subsequence that is fibonacci-like: [1,11,12], [3,11,14] or [7,11,18].
    """
    def lenLongestFibSubseq(self, arr: List[int]) -> int:
        """
        basic idea: backtracking to remove one element from the array and check if the rest of the array is a valid Fibonacci-like subsequence
        tle
        """
        def valid(nums: List[int]):
            if not nums:
                return 0
            
            n = len(nums)
            for i in range(2, n):
                t = nums[i - 1] + nums[i - 2]
                if t != nums[i]:
                    return False
            return True
        
        def helper(path: List[int]):
            if not path:
                return 0
            if valid(path):
                return len(path)
            max_length = 0
            for i in range(len(path)):
                max_length = max(max_length, helper(path[:i] + path[i + 1:]))
            return max_length
        return helper(arr)
    
    def lenLongestFibSubseq(self, arr: List[int]) -> int:
        num_set = set(arr)
        @cache
        def helper(x: int, y: int):
            if x + y not in num_set:
                return 2
            return 1 + helper(y, x + y)
        m = len(arr)
        max_length = 0
        for i in range(m):
            for j in range(i + 1, m):
                max_length = max(max_length, helper(arr[i], arr[j]))
        return max_length if max_length > 2 else 0
    
    def lenLongestFibSubseq(self, arr: List[int]) -> int:
        # Map values to indices for fast lookup
        indexes = {v:i for i, v in enumerate(arr)}
        # Dictionary to store the length of Fibonacci-like subsequences
        dp = {}
        max_len = 0
        n = len(arr)
        # Iterate over all pairs (arr[i], arr[j]) as potential Fibonacci starts
        for j in range(n):
            for i in range(j):
                x, y = arr[i], arr[j]
                # Check if Fibonacci condition holds
                if x + y in indexes:
                    # Find the index of the next Fibonacci number
                    k = indexes[x + y]
                    # Extend the sequence length
                    dp[(j, k)] = dp.get((i, j), 2) + 1
                    # Update max length
                    max_len = max(max_len, dp[(j, k)])
        return max_len