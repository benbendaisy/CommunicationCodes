class Solution:
    """
    You are given an integer array nums of length n and a 2D array queries where queries[i] = [li, ri, vali].

    Each queries[i] represents the following action on nums:

    Decrement the value at each index in the range [li, ri] in nums by at most vali.
    The amount by which each value is decremented can be chosen independently for each index.
    A Zero Array is an array with all its elements equal to 0.

    Return the minimum possible non-negative value of k, such that after processing the first k queries in sequence, nums becomes a Zero Array. If no such k exists, return -1.

    Example 1:

    Input: nums = [2,0,2], queries = [[0,2,1],[0,2,1],[1,1,3]]

    Output: 2

    Explanation:

    For i = 0 (l = 0, r = 2, val = 1):
    Decrement values at indices [0, 1, 2] by [1, 0, 1] respectively.
    The array will become [1, 0, 1].
    For i = 1 (l = 0, r = 2, val = 1):
    Decrement values at indices [0, 1, 2] by [1, 0, 1] respectively.
    The array will become [0, 0, 0], which is a Zero Array. Therefore, the minimum value of k is 2.
    Example 2:

    Input: nums = [4,3,2,1], queries = [[1,3,2],[0,2,1]]

    Output: -1

    Explanation:

    For i = 0 (l = 1, r = 3, val = 2):
    Decrement values at indices [1, 2, 3] by [2, 2, 1] respectively.
    The array will become [4, 1, 0, 0].
    For i = 1 (l = 0, r = 2, val = 1):
    Decrement values at indices [0, 1, 2] by [1, 1, 0] respectively.
    The array will become [3, 0, 0, 0], which is not a Zero Array.
    """
    def minZeroArray1(self, nums: List[int], queries: List[List[int]]) -> int:
        def helper(index):
            if all(x == 0 for x in nums):
                return index
            if index >= len(queries):
                return -1
            
            l, r, val = queries[index]
            
            # Try decrementing values independently
            for i in range(l, r + 1):
                nums[i] = max(0, nums[i] - val)
            
            return helper(index + 1)
        
        return helper(0)
    
    def minZeroArray2(self, nums: List[int], queries: List[List[int]]) -> int:
        if not nums or all(x == 0 for x in nums):
            return 0
        for i, (l, r, val) in enumerate(queries):
            for j in range(l, r + 1):
                nums[j] = max(0, nums[j] - val)  # Ensure non-negative values
            if all(x == 0 for x in nums):  # Check if the array is fully zero
                return i + 1  # Return the count of queries applied
        return -1  # If zero array is never achieved
    
    def minZeroArray(self, nums: List[int], queries: List[List[int]]) -> int:
        n = len(nums)
        total_sum = 0
        k = 0
        difference_array = [0] * (n + 1)

        # Iterate through nums
        for index in range(n):
            # Iterate through queries while current index of nums cannot equal zero
            while total_sum + difference_array[index] < nums[index]:
                k += 1

                # Zero array isn't formed after all queries are processed
                if k > len(queries):
                    return -1

                left, right, val = queries[k - 1]

                # Process start and end of range
                if right >= index:
                    difference_array[max(left, index)] += val
                    difference_array[right + 1] -= val

            # Update prefix sum at current index
            total_sum += difference_array[index]

        return k