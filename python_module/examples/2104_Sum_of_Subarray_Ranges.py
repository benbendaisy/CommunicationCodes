class Solution:
    """
    Example 1:

    Input: nums = [1,2,3]
    Output: 4
    Explanation: The 6 subarrays of nums are the following:
    [1], range = largest - smallest = 1 - 1 = 0 
    [2], range = 2 - 2 = 0
    [3], range = 3 - 3 = 0
    [1,2], range = 2 - 1 = 1
    [2,3], range = 3 - 2 = 1
    [1,2,3], range = 3 - 1 = 2
    So the sum of all ranges is 0 + 0 + 0 + 1 + 1 + 2 = 4.
    Example 2:

    Input: nums = [1,3,3]
    Output: 4
    Explanation: The 6 subarrays of nums are the following:
    [1], range = largest - smallest = 1 - 1 = 0
    [3], range = 3 - 3 = 0
    [3], range = 3 - 3 = 0
    [1,3], range = 3 - 1 = 2
    [3,3], range = 3 - 3 = 0
    [1,3,3], range = 3 - 1 = 2
    So the sum of all ranges is 0 + 0 + 0 + 2 + 0 + 2 = 4.
    Example 3:

    Input: nums = [4,-2,-3,4,1]
    Output: 59
    Explanation: The sum of all subarray ranges of nums is 59.
    """
    def subArrayRanges0(self, nums: List[int]) -> int:
        n = len(nums)
        res = 0
        for left in range(n):
            min_val, max_val = math.inf, -math.inf
            for right in range(left, n):
                max_val = max(max_val, nums[right])
                min_val = min(min_val, nums[right])
                res += max_val - min_val
        return res
    
    def subArrayRanges1(self, nums: List[int]) -> int:
        """
        Time complexity: O(n^3)
        Time limit exceeded
        """
        if not nums:
            return 0
        
        n = len(nums)
        def find_range(left: int, right: int) -> int:
            min_num = min(nums[left: right + 1])
            max_num = max(nums[left: right + 1])
            return max_num - min_num
        
        range_sums = 0
        for i in range(n):
            for j in range(i + 1, n):
                range_sums += find_range(i, j)
        return range_sums
    
    def subArrayRanges2(self, nums: List[int]) -> int:
        if not nums:
            return 0
        
        n = len(nums)
        range_sums = 0
        for i in range(n):
            max_num, min_num = nums[i], nums[i]
            for j in range(i, n):
                max_num = max(max_num, nums[j])
                min_num = min(min_num, nums[j])
                range_sums += max_num - min_num
        return range_sums
    
    def subArrayRanges3(self, nums: List[int]) -> int:
        if not nums:
            return 0
        
        n = len(nums)
        @cache
        def helper(left: int, right: int) -> int:
            if left > right:
                return 0
            
            max_num = max(nums[left:right + 1])
            min_num = min(nums[left:right + 1])
            range_num = max_num - min_num
            return range_num + helper(left + 1, right) + helper(left, right - 1) - helper(left + 1, right - 1)

        return helper(0, n - 1)
    
    def subArrayRanges4(self, nums: List[int]) -> int:
        def sum_of_extremes(nums: List[int], is_max: bool) -> int:
            stack = []
            result = 0
            # Append a sentinel value to force stack cleanup
            nums.append(float('inf') if is_max else float('-inf'))
            for i, num in enumerate(nums):
                # Use a separate condition for clarity
                while stack and (nums[stack[-1]] < num if is_max else nums[stack[-1]] > num):
                    j = stack.pop()
                    left = stack[-1] if stack else -1
                    result += nums[j] * (j - left) * (i - j)
                stack.append(i)
            return result

        return sum_of_extremes(nums.copy(), True) - sum_of_extremes(nums.copy(), False)
    
    def subArrayRanges5(self, nums: List[int]) -> int:
        def sum_of_extremes(nums: List[int], is_max: bool) -> int:
            stack, res = [], 0
            n = len(nums)
            nums.append(float('inf') if is_max else float('-inf'))
            for i, val in enumerate(nums):
                while stack and (nums[stack[-1]] < val if is_max else nums[stack[-1]] > val):
                    right = stack.pop()
                    left = stack[-1] if stack else -1
                    res += nums[right] * (right - left) * (i - right)
                stack.append(i)
            return res
        return sum_of_extremes(nums.copy(), True) - sum_of_extremes(nums.copy(), False)
    
    def subArrayRanges6(self, nums: List[int]) -> int:
        def helper(start, end, curr_min, curr_max):
            # Base case: when end reaches the length of nums
            if end == len(nums):
                return 0
            
            # Update min and max dynamically
            curr_min = min(curr_min, nums[end])
            curr_max = max(curr_max, nums[end])
            
            # Compute range and add recursive results
            range_sum = curr_max - curr_min
            return range_sum + helper(start, end + 1, curr_min, curr_max)
        
        total_sum = 0
        for i in range(len(nums)):
            total_sum += helper(i, i, nums[i], nums[i])  # Start recursion from each index
        
        return total_sum
    
    def subArrayRanges(self, nums: List[int]) -> int:
        n = len(nums)
        @cache
        def helper(idx: int, curr_min: int, curr_max: int) -> int:
            if idx == n:
                return 0
            curr_min = min(curr_min, nums[idx])
            curr_max = max(curr_max, nums[idx])
            range_sum = curr_max - curr_min
            return range_sum + helper(idx + 1, curr_min, curr_max)
        
        range_sum = 0
        for i in range(n):
            range_sum += helper(i, nums[i], nums[i])
        return range_sum
    
    def subArrayRanges(self, nums: List[int]) -> int:
        if not nums:
            return 0
        
        self.sums = 0
        n = len(nums)

        def helper(end: int, cur_min: int, cur_max: int):
            if end == n:
                return
            cur_max = max(cur_max, nums[end])
            cur_min = min(cur_min, nums[end])
            self.sums += cur_max - cur_min
            helper(end + 1, cur_min, cur_max)
        
        for start in range(n):
            helper(start, nums[start], nums[start])
        
        return self.sums