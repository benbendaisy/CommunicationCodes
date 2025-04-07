class Solution:
    """
    You are given a 0-indexed integer array nums of length n. You are initially standing at index 0. You can jump from index i to index j where i < j if:

    nums[i] <= nums[j] and nums[k] < nums[i] for all indexes k in the range i < k < j, or
    nums[i] > nums[j] and nums[k] >= nums[i] for all indexes k in the range i < k < j.
    You are also given an integer array costs of length n where costs[i] denotes the cost of jumping to index i.

    Return the minimum cost to jump to the index n - 1.


    Example 1:

    Input: nums = [3,2,4,4,1], costs = [3,7,6,4,2]
    Output: 8
    Explanation: You start at index 0.
    - Jump to index 2 with a cost of costs[2] = 6.
    - Jump to index 4 with a cost of costs[4] = 2.
    The total cost is 8. It can be proven that 8 is the minimum cost needed.
    Two other possible paths are from index 0 -> 1 -> 4 and index 0 -> 2 -> 3 -> 4.
    These have a total cost of 9 and 12, respectively.
    Example 2:

    Input: nums = [0,1,2], costs = [1,1,1]
    Output: 2
    Explanation: Start at index 0.
    - Jump to index 1 with a cost of costs[1] = 1.
    - Jump to index 2 with a cost of costs[2] = 1.
    The total cost is 2. Note that you cannot jump directly from index 0 to index 2 because nums[0] <= nums[1].
    """
    def minCost1(self, nums: List[int], costs: List[int]) -> int:
        """
        Time limit exceeded
        """
        n = len(nums)
        dp = [float('inf')] * n  # Min cost to reach each index
        dp[0] = 0  # Starting position has 0 cost
        
        queue = deque([0])  # BFS queue initialized with starting index
        
        while queue:
            i = queue.popleft()
            
            for j in range(i + 1, n):
                valid_jump = True
                if nums[i] <= nums[j]:
                    for k in range(i + 1, j):
                        if nums[k] >= nums[i]:
                            valid_jump = False
                            break
                else:  # nums[i] > nums[j]
                    for k in range(i + 1, j):
                        if nums[k] < nums[i]:
                            valid_jump = False
                            break
                
                if valid_jump:
                    new_cost = dp[i] + costs[j]
                    if new_cost < dp[j]:
                        dp[j] = new_cost
                        queue.append(j)
        
        return dp[n - 1]
    
    def minCost2(self, nums: List[int], costs: List[int]) -> int:
        n = len(nums)
        dp = [float('inf')] * n
        dp[0] = 0
        
        # Next greater or equal element with all in between < nums[i]
        next_ge = [n] * n
        stack = []
        for i in range(n):
            while stack and nums[stack[-1]] <= nums[i]:
                next_ge[stack.pop()] = i
            stack.append(i)
        
        # Next smaller element with all in between >= nums[i]
        next_s = [n] * n
        stack = []
        for i in range(n):
            while stack and nums[stack[-1]] > nums[i]:
                next_s[stack.pop()] = i
            stack.append(i)
        
        # We can process indices in order, since jumps are to the right
        for i in range(n):
            if dp[i] == float('inf'):
                continue
            # Check next_ge[i]
            j = next_ge[i]
            if j < n:
                if dp[i] + costs[j] < dp[j]:
                    dp[j] = dp[i] + costs[j]
            # Check next_s[i]
            j = next_s[i]
            if j < n:
                if dp[i] + costs[j] < dp[j]:
                    dp[j] = dp[i] + costs[j]
        
        return dp[-1]
    
    def minCost3(self, nums: List[int], costs: List[int]) -> int:
        n = len(nums)
        dp = [float('inf')] * n
        dp[0] = 0

        next_ge = [n] * n
        stack = []
        for i in range(n):
            while stack and nums[stack[-1]] <= nums[i]:
                next_ge[stack.pop()] = i
            stack.append(i)
        
        next_s = [n] * n
        stack = []
        for i in range(n):
            while stack and nums[stack[-1]] > nums[i]:
                next_s[stack.pop()] = i
            stack.append(i)
        
        for i in range(n):
            if dp[i] == float('inf'):
                continue
            
            j = next_ge[i]
            if j < n and dp[i] + costs[j] < dp[j]:
                dp[j] = dp[i] + costs[j]
            
            j = next_s[i]
            if j < n and dp[i] + costs[j] < dp[j]:
                dp[j] = dp[i] + costs[j]
            
        return dp[-1]

     def minCost(self, nums: List[int], costs: List[int]) -> int:
        n = len(nums)
        dp = [float('inf')] * n
        dp[0] = 0

        next_ge, next_s = [], []

        for i in range(n):
            while next_ge and nums[next_ge[-1]] <= nums[i]:
                dp[i] = min(dp[i], dp[next_ge.pop()] + costs[i])
            while next_s and nums[next_s[-1]] > nums[i]:
                dp[i] = min(dp[i], dp[next_s.pop()] + costs[i])
            next_ge.append(i)
            next_s.append(i)
            
        return dp[-1]