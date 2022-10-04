from collections import defaultdict
from typing import List


class Solution:
    """
        Given two integer arrays nums1 and nums2, return the maximum length of a subarray that appears in both arrays.

        Example 1:

        Input: nums1 = [1,2,3,2,1], nums2 = [3,2,1,4,7]
        Output: 3
        Explanation: The repeated subarray with maximum length is [3,2,1].
        Example 2:

        Input: nums1 = [0,0,0,0,0], nums2 = [0,0,0,0,0]
        Output: 5

        Constraints:

        1 <= nums1.length, nums2.length <= 1000
        0 <= nums1[i], nums2[i] <= 100
    """
    def findLength1(self, nums1: List[int], nums2: List[int]) -> int:
        ans = 0
        bStarts = defaultdict(list)
        for i, v in enumerate(nums2):
            bStarts[v].append(i)

        for i, v in enumerate(nums1):
            for j in bStarts[v]:
                k = 0
                while i + k < len(nums1) and j + k < len(nums2) and nums1[i + k] == nums2[j + k]:
                    k += 1
                ans = max(ans, k)
        return ans

    def findLength2(self, nums1: List[int], nums2: List[int]) -> int:
        m, n = len(nums1), len(nums2)
        memo = [[0] * (n + 1) for _ in range(m + 1)]
        for i in range(1, m + 1):
            for j in range(1, n + 1):
                if nums1[i] == nums2[j]:
                    memo[i][j] = memo[i - 1][j - 1] + 1

        return max(max(row) for row in memo)

    def findLength(self, nums1: List[int], nums2: List[int]) -> int:
        m, n = len(nums1), len(nums2)
        memo = [[0] * (n + 1) for _ in range(m + 1)]
        for i in range(1, m + 1):
            for j in range(1, n + 1):
                if nums1[i - 1] == nums2[j - 1]:
                    memo[i][j] = memo[i - 1][j - 1] + 1

        return max(max(row) for row in memo)