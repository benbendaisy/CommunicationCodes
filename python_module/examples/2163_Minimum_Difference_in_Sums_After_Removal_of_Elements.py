class Solution:
    """
    You are given a 0-indexed integer array nums consisting of 3 * n elements.

    You are allowed to remove any subsequence of elements of size exactly n from nums. The remaining 2 * n elements will be divided into two equal parts:

    The first n elements belonging to the first part and their sum is sumfirst.
    The next n elements belonging to the second part and their sum is sumsecond.
    The difference in sums of the two parts is denoted as sumfirst - sumsecond.

    For example, if sumfirst = 3 and sumsecond = 2, their difference is 1.
    Similarly, if sumfirst = 2 and sumsecond = 3, their difference is -1.
    Return the minimum difference possible between the sums of the two parts after the removal of n elements.

    Example 1:

    Input: nums = [3,1,2]
    Output: -1
    Explanation: Here, nums has 3 elements, so n = 1. 
    Thus we have to remove 1 element from nums and divide the array into two equal parts.
    - If we remove nums[0] = 3, the array will be [1,2]. The difference in sums of the two parts will be 1 - 2 = -1.
    - If we remove nums[1] = 1, the array will be [3,2]. The difference in sums of the two parts will be 3 - 2 = 1.
    - If we remove nums[2] = 2, the array will be [3,1]. The difference in sums of the two parts will be 3 - 1 = 2.
    The minimum difference between sums of the two parts is min(-1,1,2) = -1. 
    Example 2:

    Input: nums = [7,9,5,8,1,3]
    Output: 1
    Explanation: Here n = 2. So we must remove 2 elements and divide the remaining array into two parts containing two elements each.
    If we remove nums[2] = 5 and nums[3] = 8, the resultant array will be [7,9,1,3]. The difference in sums will be (7+9) - (1+3) = 12.
    To obtain the minimum difference, we should remove nums[1] = 9 and nums[4] = 1. The resultant array becomes [7,5,8,3]. The difference in sums of the two parts is (7+5) - (8+3) = 1.
    It can be shown that it is not possible to obtain a difference smaller than 1.
    """
    def minimumDifference1(self, nums: List[int]) -> int:
        max_int = 10000
        if not nums or len(nums) % 3 != 0:
            return max_int
        n = len(nums) // 3

        @cache
        def helper(arr: tuple, cuts: int):
            if cuts == n:
                return sum(arr[:n]) - sum(arr[n:])
            
            min_diff = max_int
            for i, v in enumerate(arr):
                new_arr = arr[:i] + arr[i + 1:]
                diff = helper(new_arr, cuts + 1)
                min_diff = min(min_diff, diff)
            
            return min_diff
        
        return helper(tuple(nums), 0)
    
    def minimumDifference2(self, nums: List[int]) -> int:
        n = len(nums) // 3
        
        # 1. Calculate Prefix Minimums
        # prefix_mins[i] will store the sum of the n smallest elements in nums[0...i]
        prefix_mins = [0] * (3 * n)
        max_heap = []
        current_sum = 0
        for i in range(3 * n):
            heapq.heappush(max_heap, -nums[i]) # Use negative for max-heap behavior
            current_sum += nums[i]
            
            if len(max_heap) > n:
                largest_val = -heapq.heappop(max_heap)
                current_sum -= largest_val

            if len(max_heap) == n:
                prefix_mins[i] = current_sum

        # 2. Calculate Suffix Maximums
        # suffix_maxs[i] will store the sum of the n largest elements in nums[i...3n-1]
        suffix_maxs = [0] * (3 * n)
        min_heap = []
        current_sum = 0
        for i in range(3 * n - 1, -1, -1):
            heapq.heappush(min_heap, nums[i])
            current_sum += nums[i]
            
            if len(min_heap) > n:
                smallest_val = heapq.heappop(min_heap)
                current_sum -= smallest_val

            if len(min_heap) == n:
                suffix_maxs[i] = current_sum

        # 3. Find the Minimum Difference
        # Iterate through all possible split points 'i'.
        # The split is between index i-1 and i.
        # The first part is nums[:i], the second is nums[i:].
        min_diff = float('inf')
        for i in range(n, 2 * n + 1):
            # The sum of n smallest from the left part (nums[0...i-1])
            left_sum = prefix_mins[i-1]
            
            # The sum of n largest from the right part (nums[i...3n-1])
            right_sum = suffix_maxs[i]
            
            min_diff = min(min_diff, left_sum - right_sum)
            
        return min_diff