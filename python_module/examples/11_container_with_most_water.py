from typing import List


class Solution:
    def maxArea1(self, height: List[int]) -> int:
        if not height:
            return 0
        n = len(height)
        area = 0

        l, r = 0, n - 1
        while l <= r:
            area = max(area, min(height[l], height[r]) * (r - l))
            if height[l] < height[r]:
                l += 1
            else:
                r -= 1
        return area

    def maxArea2(self, height: List[int]) -> int:
        max_area = 0
        l, r = 0, len(height) - 1
        while l < r:
            area = (r - l) * min(height[l], height[r])
            max_area = max(max_area, area)
            if height[l] < height[r]:
                l += 1
            else:
                r -= 1
        return max_area

    def maxArea3(self, height: List[int]) -> int:
        max_area = 0
        left, right = 0, len(height) - 1
        while left < right:
            local_area = min(height[left], height[right]) * (right - left)
            max_area = max(max_area, local_area)
            if height[left] < height[right]:
                left += 1
            else:
                right -= 1
        return max_area
    
    def maxArea(self, height: List[int]) -> int:
        max_area, n = 0, len(height)
        left, right = 0, n - 1
        while left < right:
            max_area = max(max_area, min(height[left], height[right]) * (right - left))
            if height[left] < height[right]:
                left += 1
            else:
                right -= 1
        return max_area

if __name__ == "__main__":
    height = [1,8,6,2,5,4,8,3,7]
    solution = Solution()
    ret = solution.maxArea(height)
    print(ret)