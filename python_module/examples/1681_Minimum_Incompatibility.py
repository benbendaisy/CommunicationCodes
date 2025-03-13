class Solution:
    """
    You are given an integer array nums​​​ and an integer k. You are asked to distribute this array into k subsets of equal size such that there are no two equal elements in the same subset.

    A subset's incompatibility is the difference between the maximum and minimum elements in that array.

    Return the minimum possible sum of incompatibilities of the k subsets after distributing the array optimally, or return -1 if it is not possible.

    A subset is a group integers that appear in the array with no particular order.

    Example 1:

    Input: nums = [1,2,1,4], k = 2
    Output: 4
    Explanation: The optimal distribution of subsets is [1,2] and [1,4].
    The incompatibility is (2-1) + (4-1) = 4.
    Note that [1,1] and [2,4] would result in a smaller sum, but the first subset contains 2 equal elements.
    Example 2:

    Input: nums = [6,3,8,1,3,1,2,2], k = 4
    Output: 6
    Explanation: The optimal distribution of subsets is [1,2], [2,3], [6,8], and [1,3].
    The incompatibility is (2-1) + (3-2) + (8-6) + (3-1) = 6.
    Example 3:

    Input: nums = [5,3,3,6,3,3], k = 3
    Output: -1
    Explanation: It is impossible to distribute nums into 3 subsets where no two elements are equal in the same subset.
    """
    def minimumIncompatibility1(self, nums: List[int], k: int) -> int:
        n = len(nums)
        if n % k != 0:
            return -1
        m = n // k
        def helper(idx: int):
            if idx == n:
                sums = 0
                for i in range(k):
                    sums += max(arr[i]) - min(arr[i])
                return sums
            
            min_sum = float('inf')
            for i in range(k):
                if len(arr[i]) < m and nums[idx] not in arr[i]:
                    arr[i].append(nums[idx])
                    min_sum = min(min_sum, helper(idx + 1))
                    arr[i].pop()
            return min_sum
        arr = [[] for _ in range(k)]
        res = helper(0)
        return -1 if res == float('inf') else res
    
    def minimumIncompatibility(self, nums: List[int], k: int) -> int:
        nums.sort()
        
        def fn(i, cand=0, ans=inf):
            """Return minimum incompatibility via backtracking."""
            if cand + len(nums) - i - sum(not x for x in stack) >= ans: return ans # early return 
            if i == len(nums): return cand
            for ii in range(k): 
                if len(stack[ii]) < len(nums)//k and (not stack[ii] or stack[ii][-1] != nums[i]) and (not ii or stack[ii-1] != stack[ii]): 
                    stack[ii].append(nums[i])
                    if len(stack[ii]) == 1: ans = fn(i+1, cand, ans)
                    else: ans = fn(i+1, cand + stack[ii][-1] - stack[ii][-2], ans)
                    stack[ii].pop()
            return ans 
        
        stack = [[] for _ in range(k)]
        ans = fn(0)
        return ans if ans < inf else -1