class Solution:
    """
    Given an integer array nums and an integer k, return true if it is possible to divide this array into k non-empty subsets whose sums are all equal.

    Example 1:

    Input: nums = [4,3,2,3,5,2,1], k = 4
    Output: true
    Explanation: It is possible to divide it into 4 subsets (5), (1, 4), (2,3), (2,3) with equal sums.
    Example 2:

    Input: nums = [1,2,3,4], k = 3
    Output: false
    """
    def canPartitionKSubsets1(self, nums: List[int], k: int) -> bool:
        sums = sum(nums)
        if k == 0 or sums % k != 0:
            return False
        ave = sums // k
        n = len(nums)
        arr = [0] * k
        
        def helper(idx: int) -> int:
            if idx == n:
                return all(x == ave for x in arr)
            
            for i in range(k):
                arr[i] += nums[idx]
                if helper(idx + 1):
                    return True
                arr[i] -= nums[idx]
            return False
        
        return helper(0)
    
    def canPartitionKSubsets2(self, nums: List[int], k: int) -> bool:
        total_sum = sum(nums)
        if k == 0 or total_sum % k != 0:
            return False
        target = total_sum // k
        nums.sort(reverse=True)  # Sorting in descending order for efficiency
        n = len(nums)
        stack = deque([(0, [0] * k)])  # Stack storing (index, subset_sums list)

        while stack:
            idx, subset_sums = stack.pop()
            if idx == n:
                if all(x == target for x in subset_sums):
                    return True
                continue

            for i in range(k):
                if subset_sums[i] + nums[idx] > target:
                    continue
                subset_sums[i] += nums[idx]
                stack.append((idx + 1, subset_sums[:]))  # Push next state
                subset_sums[i] -= nums[idx]  # Backtrack
                
                if subset_sums[i] == 0:
                    break  # Optimization: Avoid redundant work
        
        return False
    
    def canPartitionKSubsets(self, nums: List[int], k: int) -> bool:
        total_sum = sum(nums)
        if k == 0 or total_sum % k != 0:
            return False
        
        target = total_sum // k
        n, stack = len(nums), deque([(0, [0] * k)])

        while stack:
            idx, arr = stack.pop()
            if idx == n:
                if all(x == target for x in arr):
                    return True
                continue
            
            for i in range(k):
                if arr[i] + nums[idx] > target:
                    continue
                arr[i] += nums[idx]
                stack.append((idx + 1, arr[:]))
                arr[i] -= nums[idx]

                if arr[i] == 0:
                    break
        return False