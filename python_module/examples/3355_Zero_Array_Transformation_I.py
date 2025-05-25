class Solution:
    """
    You are given an integer array nums of length n and a 2D array queries, where queries[i] = [li, ri].

    For each queries[i]:

    Select a subset of indices within the range [li, ri] in nums.
    Decrement the values at the selected indices by 1.
    A Zero Array is an array where all elements are equal to 0.

    Return true if it is possible to transform nums into a Zero Array after processing all the queries sequentially, otherwise return false.

    Example 1:

    Input: nums = [1,0,1], queries = [[0,2]]

    Output: true

    Explanation:

    For i = 0:
    Select the subset of indices as [0, 2] and decrement the values at these indices by 1.
    The array will become [0, 0, 0], which is a Zero Array.
    Example 2:

    Input: nums = [4,3,2,1], queries = [[1,3],[0,2]]

    Output: false

    Explanation:

    For i = 0:
    Select the subset of indices as [1, 2, 3] and decrement the values at these indices by 1.
    The array will become [4, 2, 1, 0].
    For i = 1:
    Select the subset of indices as [0, 1, 2] and decrement the values at these indices by 1.
    The array will become [3, 1, 0, 0], which is not a Zero Array.
    """
    def isZeroArray1(self, nums: List[int], queries: List[List[int]]) -> bool:
        if not nums:
            return False
        
        num_queries = len(queries)
        @cache
        def helper(current_query_idx: int, current_state: tuple) -> bool:
            if current_query_idx == num_queries:
                return all(x == 0 for x in current_state)
            
            l, r = queries[current_query_idx]
            
            new_state_list = list(current_state)
            for i in range(l, r + 1):
                if new_state_list[i] > 0:
                    new_state_list[i] -= 1
                    if helper(current_query_idx + 1, tuple(new_state_list)):
                        return True
                elif helper(current_query_idx + 1, tuple(new_state_list)):
                        return True
            return False
        return helper(0, tuple(nums))
    
    def isZeroArray2(self, nums: List[int], queries: List[List[int]]) -> bool:
        deltaArray = [0] * (len(nums) + 1)
        for left, right in queries:
            deltaArray[left] += 1
            deltaArray[right + 1] -= 1
        operationCounts = []
        currentOperations = 0
        for delta in deltaArray:
            currentOperations += delta
            operationCounts.append(currentOperations)
        for operations, target in zip(operationCounts, nums):
            if operations < target:
                return False
        return True
    
    def isZeroArray3(self, nums, queries):
        n = len(nums)
        sweep = [0] * (n + 1)

        for l, r in queries:
            sweep[l] += 1
            if r + 1 <= n:
                sweep[r + 1] -= 1

        for i in range(1, n + 1):
            sweep[i] += sweep[i - 1]

        for i in range(n):
            if sweep[i] < nums[i]:
                return False

        return True
    
    def isZeroArray4(self, nums: List[int], queries: List[List[int]]) -> bool:
        n = len(nums)
        sweep = [0] * (n + 1)

        # Apply sweep line technique to build difference array
        for l, r in queries:
            sweep[l] += 1
            if r + 1 <= n:
                sweep[r + 1] -= 1

        # Use accumulate to compute prefix sum
        prefix = list(accumulate(sweep))

        # Compare prefix[i] (operations applied) with nums[i]
        return all(prefix[i] >= nums[i] for i in range(n))