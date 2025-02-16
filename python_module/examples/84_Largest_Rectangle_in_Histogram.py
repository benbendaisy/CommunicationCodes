class Solution:
    """
        Given an array of integers heights representing the histogram's bar height where the width of each bar is 1, return the area of the largest rectangle in the histogram.

        Example 1:

        Input: heights = [2,1,5,6,2,3]
        Output: 10
        Explanation: The above is a histogram where width of each bar is 1.
        The largest rectangle is shown in the red area, which has an area = 10 units.
        Example 2:

        Input: heights = [2,4]
        Output: 4
    """
    def largestRectangleArea1(self, heights: List[int]) -> int:
        if not heights:
            return 0
        heights.append(0)
        stack = []
        max_area = 0
        for i, height in enumerate(heights):
            while stack and heights[stack[-1]] >= height:
                cur = stack.pop()
                left = stack[-1] + 1 if stack else 0
                right = i - 1
                max_area = max(max_area, (right - left + 1) * heights[cur])
            stack.append(i)
        return max_area
    
    def largestRectangleArea(self, heights: List[int]) -> int:
        if not heights:
            return 0
        heights.append(0)
        stack = []
        max_area = 0
        for i, height in enumerate(heights):
            while stack and heights[stack[-1]] >= height:
                h = heights[stack.pop()]
                w = i if not stack else i - stack[-1] - 1
                max_area = max(max_area, h * w)
            stack.append(i)
        return max_area