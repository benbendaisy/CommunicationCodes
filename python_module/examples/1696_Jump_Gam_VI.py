import heapq
from collections import deque
from functools import lru_cache
from typing import List


class Solution:
    """
        You are given a 0-indexed integer array nums and an integer k.

        You are initially standing at index 0. In one move, you can jump at most k steps forward without going outside the boundaries of the array. That is, you can jump from index i to any index in the range [i + 1, min(n - 1, i + k)] inclusive.

        You want to reach the last index of the array (index n - 1). Your score is the sum of all nums[j] for each index j you visited in the array.

        Return the maximum score you can get.

        Example 1:

        Input: nums = [1,-1,-2,4,-7,3], k = 2
        Output: 7
        Explanation: You can choose your jumps forming the subsequence [1,-1,4,3] (underlined above). The sum is 7.
        Example 2:

        Input: nums = [10,-5,-2,4,0,3], k = 3
        Output: 17
        Explanation: You can choose your jumps forming the subsequence [10,4,3] (underlined above). The sum is 17.
        Example 3:

        Input: nums = [1,-5,-20,4,-1,3,-6,-3], k = 2
        Output: 0

        Constraints:

        1 <= nums.length, k <= 105
        -104 <= nums[i] <= 104
    """
    def maxResult1(self, nums: List[int], k: int) -> int:
        if not nums:
            return -1
        minValue = -1000001
        @lru_cache(None)
        def findMaxResult(idx: int):
            if idx == len(nums):
                return 0
            maxValue = minValue
            for step in range(idx, idx + k - 1):
                maxValue = max(maxValue, findMaxResult(step + 1) + nums[step])
            return maxValue

        maxValue = findMaxResult(0)
        return maxValue if maxValue != minValue else -1

    def maxResult2(self, nums: List[int], k: int) -> int:
        if not nums:
            return -1

        dp = [-10001] * len(nums)
        dp[0] = nums[0]
        for i in range(1, len(nums)):
            start = i - k if i - k > 0 else 0
            dp[i] = max(dp[start:i]) + nums[i]
        return dp[-1]

    def maxResult3(self, nums: List[int], k: int) -> int:
        if not nums:
            return -1

        n = len(nums)
        scores = [0] * n
        scores[0] = nums[0]
        pq = []
        heapq.heappush(pq, (-nums[0], 0))
        for i in range(1, n):
            while pq[0][1] < i - k:
                heapq.heappop(pq)
            scores[i] = nums[i] + scores[pq[0][1]]
            heapq.heappush(pq, (-scores[i], i))
        return scores[-1]

    def maxResult(self, nums: List[int], k: int) -> int:
        if not nums:
            return -1
        n = len(nums)
        scores = [0] * n
        scores[0] = nums[0]
        que = deque([0])
        for i in range(1, n):
            while que and que[0] < i - k:
                que.popleft()
            scores[i] = nums[i] + scores[que[0]]
            while que and scores[i] >= scores[que[-1]]:
                que.pop()
            que.append(i)
        return scores[-1]



if __name__ == "__main__":
    nums = [1,-1,-2,4,-7,3]
    k = 2
    solution = Solution()
    ret = solution.maxResult(nums, k)
    print(ret)
