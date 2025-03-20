class Solution:
    """
    You are given a binary array nums.

    You can do the following operation on the array any number of times (possibly zero):

    Choose any 3 consecutive elements from the array and flip all of them.
    Flipping an element means changing its value from 0 to 1, and from 1 to 0.

    Return the minimum number of operations required to make all elements in nums equal to 1. If it is impossible, return -1.

    Example 1:

    Input: nums = [0,1,1,1,0,0]

    Output: 3

    Explanation:
    We can do the following operations:

    Choose the elements at indices 0, 1 and 2. The resulting array is nums = [1,0,0,1,0,0].
    Choose the elements at indices 1, 2 and 3. The resulting array is nums = [1,1,1,0,0,0].
    Choose the elements at indices 3, 4 and 5. The resulting array is nums = [1,1,1,1,1,1].
    Example 2:

    Input: nums = [0,1,1,1]

    Output: -1

    Explanation:
    It is impossible to make all elements equal to 1.
    """
    def minOperations1(self, nums: List[int]) -> int:
        if not nums:
            return -1
        
        n = len(nums)

        def flip(idx: int):
            """Flips the next 3 elements starting from idx (if possible)."""
            for i in range(idx, min(idx + 3, n)):
                nums[i] ^= 1  # Flip 0 to 1 and 1 to 0

        @lru_cache(None)
        def helper(idx: int) -> int:
            """Recursive function to find the minimum flips."""
            while idx < n and nums[idx] == 1:
                idx += 1  # Skip already 1s
            
            if idx == n:
                return 0  # Successfully flipped all elements to 1
            
            if idx > n - 3:
                return float('inf')  # If less than 3 elements remain, we cannot flip
            
            # Try flipping at idx
            flip(idx)
            flip_count = helper(idx + 1)  # Move to the next position
            flip(idx)  # Backtrack
            
            return 1 + flip_count  # Count this flip operation

        res = helper(0)
        return res if res != float('inf') else -1
    
    def minOperations(self, nums: List[int]) -> int:
        if not nums:
            return -1
        n = len(nums)

        def flip(idx: int):
            for i in range(idx, min(idx + 3, n)):
                nums[i] ^= 1

        @cache
        def helper(idx: int) -> int:
            while idx < n and nums[idx] == 1:
                idx += 1
            
            if idx == n:
                return 0
            
            if idx > n - 3:
                return float('inf')
            flip(idx)
            op_cnt = helper(idx + 1)
            flip(idx)
            return op_cnt + 1
        res = helper(0)
        return res if res != float('inf') else -1