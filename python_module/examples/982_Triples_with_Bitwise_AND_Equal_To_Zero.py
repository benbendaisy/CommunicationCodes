class Solution:
    """
    Given an integer array nums, return the number of AND triples.

    An AND triple is a triple of indices (i, j, k) such that:

    0 <= i < nums.length
    0 <= j < nums.length
    0 <= k < nums.length
    nums[i] & nums[j] & nums[k] == 0, where & represents the bitwise-AND operator.

    Example 1:

    Input: nums = [2,1,3]
    Output: 12
    Explanation: We could choose the following i, j, k triples:
    (i=0, j=0, k=1) : 2 & 2 & 1
    (i=0, j=1, k=0) : 2 & 1 & 2
    (i=0, j=1, k=1) : 2 & 1 & 1
    (i=0, j=1, k=2) : 2 & 1 & 3
    (i=0, j=2, k=1) : 2 & 3 & 1
    (i=1, j=0, k=0) : 1 & 2 & 2
    (i=1, j=0, k=1) : 1 & 2 & 1
    (i=1, j=0, k=2) : 1 & 2 & 3
    (i=1, j=1, k=0) : 1 & 1 & 2
    (i=1, j=2, k=0) : 1 & 3 & 2
    (i=2, j=0, k=1) : 3 & 2 & 1
    (i=2, j=1, k=0) : 3 & 1 & 2
    Example 2:

    Input: nums = [0,0,0]
    Output: 27
    """
    def countTriplets1(self, nums: List[int]) -> int:
        n = len(nums)
        cnt = 0
        for i in range(n):
            for j in range(n):
                for k in range(n):
                    if nums[i] & nums[j] & nums[k] == 0:
                        cnt += 1
        return cnt
    
    def countTriplets2(self, nums: List[int]) -> int:
        freq = defaultdict(int)
        
        # Step 1: Precompute all (nums[i] & nums[j]) counts
        for i in nums:
            for j in nums:
                freq[i & j] += 1  # Store how many times (i & j) appears

        # Step 2: Count valid triplets where (i & j & k) == 0
        cnt = 0
        for k in nums:
            for key, count in freq.items():
                if key & k == 0:  # Valid combination
                    cnt += count
        
        return cnt
    
    def countTriplets(self, nums: List[int]) -> int:
        n = len(nums)
        res = 0
        freq = defaultdict(int)
        for i in nums:
            for j in nums:
                freq[i & j] += 1
        
        for num in nums:
            for key, cnt in freq.items():
                if key & num == 0:
                    res += cnt
        return res