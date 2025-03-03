class Solution:
    """
    You are given an array nums​​​ and an integer k​​​​​. The XOR of a segment [left, right] where left <= right is the XOR of all the elements with indices between left and right, inclusive: nums[left] XOR nums[left+1] XOR ... XOR nums[right].

    Return the minimum number of elements to change in the array such that the XOR of all segments of size k​​​​​​ is equal to zero.

    Example 1:

    Input: nums = [1,2,0,3,0], k = 1
    Output: 3
    Explanation: Modify the array from [1,2,0,3,0] to from [0,0,0,0,0].
    Example 2:

    Input: nums = [3,4,5,2,1,7,3,4,7], k = 3
    Output: 3
    Explanation: Modify the array from [3,4,5,2,1,7,3,4,7] to [3,4,7,3,4,7,3,4,7].
    Example 3:

    Input: nums = [1,2,4,1,2,5,1,2,6], k = 3
    Output: 3
    Explanation: Modify the array from [1,2,4,1,2,5,1,2,6] to [1,2,3,1,2,3,1,2,3].
    """
    def minChanges1(self, nums: List[int], k: int) -> int:
        freq = defaultdict(lambda: defaultdict(int))
        for i, x in enumerate(nums): freq[i%k][x] += 1 # freq by row
        
        n = 1 << 10
        dp = [0] + [-inf]*(n-1)
        for i in range(k): 
            mx = max(dp)
            tmp = [0]*n
            for x, c in enumerate(dp): 
                for xx, cc in freq[i].items(): 
                    tmp[x^xx] = max(tmp[x^xx], c + cc, mx)
            dp = tmp 
        return len(nums) - dp[0]
    
    def minChanges(self, nums: List[int], k: int) -> int:
        # Group the elements into k groups and count frequencies
        freq = defaultdict(lambda: defaultdict(int))
        total_counts = [0] * k  # Store total numbers in each group
        for i, x in enumerate(nums):
            freq[i % k][x] += 1
            total_counts[i % k] += 1
        
        # Recursive function to compute the minimum changes
        @cache
        def helper(idx: int, current_xor: int) -> int:
            if idx == k:
                return 0 if current_xor == 0 else float('inf')
            
            min_changes = float('inf')
            
            # Try all possible values for the current group
            for num, count in freq[idx].items():
                changes = (total_counts[idx] - count) + helper(idx + 1, current_xor ^ num)
                min_changes = min(min_changes, changes)
            
            # Also consider changing all elements in the current group to a new value
            # This ensures that the XOR can be zero even if no existing value works
            changes = total_counts[idx] + helper(idx + 1, current_xor ^ 0)
            min_changes = min(min_changes, changes)
            
            return min_changes
        
        # Start the recursion with the first group and initial XOR value of 0
        return helper(0, 0)