class Solution:
    """
    Given a 0-indexed integer array nums, return the number of distinct quadruplets (a, b, c, d) such that:

    nums[a] + nums[b] + nums[c] == nums[d], and
    a < b < c < d
    
    Example 1:

    Input: nums = [1,2,3,6]
    Output: 1
    Explanation: The only quadruplet that satisfies the requirement is (0, 1, 2, 3) because 1 + 2 + 3 == 6.
    Example 2:

    Input: nums = [3,3,6,4,5]
    Output: 0
    Explanation: There are no such quadruplets in [3,3,6,4,5].
    Example 3:

    Input: nums = [1,1,1,3,5]
    Output: 4
    Explanation: The 4 quadruplets that satisfy the requirement are:
    - (0, 1, 2, 3): 1 + 1 + 1 == 3
    - (0, 1, 3, 4): 1 + 1 + 3 == 5
    - (0, 2, 3, 4): 1 + 1 + 3 == 5
    - (1, 2, 3, 4): 1 + 1 + 3 == 5
    """
    def countQuadruplets1(self, nums: List[int]) -> int:
        if not nums:
            return 0
        n, cnt = len(nums), 0
        for i in range(n):
            for j in range(i + 1, n):
                for k in range(j + 1, n):
                    for l in range(k + 1, n):
                        if nums[i] + nums[j] + nums[k] == nums[l]:
                            cnt += 1
        return cnt
    
    def countQuadruplets(self, nums: List[int]) -> int:
        n, cnt = len(nums), 0
        freq = defaultdict(int)

        # Iterate in reverse order to maintain count of possible `nums[l]` values
        for k in range(n - 2, 1, -1):
            freq[nums[k + 1]] += 1  # Update count of nums[l]
            
            for i in range(k):
                for j in range(i + 1, k):
                    target = nums[i] + nums[j] + nums[k]
                    cnt += freq[target]  # Check if target exists in freq

        return cnt