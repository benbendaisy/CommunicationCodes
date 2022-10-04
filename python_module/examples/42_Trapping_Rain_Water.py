from collections import deque
from typing import List


class Solution:
    """
        Given n non-negative integers representing an elevation map where the width of each bar is 1, compute how much water it can trap after raining.

        Example 1:

        Input: height = [0,1,0,2,1,0,1,3,2,1,2,1]
        Output: 6
        Explanation: The above elevation map (black section) is represented by array [0,1,0,2,1,0,1,3,2,1,2,1]. In this case, 6 units of rain water (blue section) are being trapped.
        Example 2:

        Input: height = [4,2,0,3,2,5]
        Output: 9

        Constraints:

        n == height.length
        1 <= n <= 2 * 104
        0 <= height[i] <= 105
    """
    def trap1(self, height: List[int]) -> int:
        if not height:
            return 0
        n = len(height)
        leftMax = [0] * n
        rightMax = [0] * n
        leftMax[0] = height[0]
        rightMax[-1] = height[-1]

        for i in range(1, n):
            leftMax[i] = max(height[i], leftMax[i - 1])

        for i in range(n - 2, 0, -1):
            rightMax[i] = max(height[i], rightMax[i + 1])

        ans = 0
        for i in range(1, n):
            ans += min(leftMax[i], rightMax[i]) - height[i]

        return ans

    def trap(self, height: List[int]) -> int:
        if not height:
            return 0

        stack = []
        res = 0
        for cur in range(len(height)):
            while stack and height[cur] > height[stack[-1]]:
                h = height[stack.pop()]
                if not stack:
                    break
                res += (min(height[stack[-1]], height[cur]) - h) * (cur - stack[-1] - 1)
            stack.append(cur)

        return res


