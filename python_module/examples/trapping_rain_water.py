from collections import deque
from typing import List


class Solution:
    def trap1(self, height: List[int]) -> int:
        if not height:
            return 0

        l, r = [0] * len(height), [0] * len(height)
        l[0], r[len(height) - 1] = height[0], height[len(height) - 1]

        for i in range(1, len(height)):
            l[i] = max(l[i - 1], height[i])
            r[-i] = max(r[-i + 1], height[-i])

        res = 0
        for i in range(1, len(height) - 1):
            res += min(l[i], r[i]) - height[i]

        return res

    def trap(self, height: List[int]) -> int:
        if not height:
            return 0

        q = deque()
        res = 0
        for cur in range(len(height)):
            while q and height[q[-1]] < height[cur]:
                h = height[q.pop()]
                if not q:
                    break
                res += (min(height[q[-1]], height[cur]) - h) * (cur - q[-1] - 1)
            q.append(cur)
        return res

if __name__ == "__main__":
    height = [4,2,0,3,2,5]
    solution = Solution()
    ret = solution.trap(height)
    print(ret)