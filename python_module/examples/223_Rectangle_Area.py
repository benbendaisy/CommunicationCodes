class Solution:
    """
        Given the coordinates of two rectilinear rectangles in a 2D plane, return the total area covered by the two rectangles.

        The first rectangle is defined by its bottom-left corner (ax1, ay1) and its top-right corner (ax2, ay2).

        The second rectangle is defined by its bottom-left corner (bx1, by1) and its top-right corner (bx2, by2).

        Example 1:

        Rectangle Area
        Input: ax1 = -3, ay1 = 0, ax2 = 3, ay2 = 4, bx1 = 0, by1 = -1, bx2 = 9, by2 = 2
        Output: 45
        Example 2:

        Input: ax1 = -2, ay1 = -2, ax2 = 2, ay2 = 2, bx1 = -2, by1 = -2, bx2 = 2, by2 = 2
        Output: 16
    """
    def computeArea(self, ax1: int, ay1: int, ax2: int, ay2: int, bx1: int, by1: int, bx2: int, by2: int) -> int:
        area_a = (ay2 - ay1) * (ax2 - ax1)
        area_b = (by2 - by1) * (bx2 - bx1)

        # calculate x overlap
        left, right = max(ax1, bx1), min(ax2, bx2)
        x_overlap = right - left

        # calculate y overlap
        bottom, top = max(ay1, by1), min(ay2, by2)
        y_overlap = top - bottom

        area_of_overlap = 0
        # if the rectangles overlap each other, then calculate
        # the area of the overlap
        if x_overlap > 0 and y_overlap > 0:
            area_of_overlap = y_overlap * x_overlap

        # area_of_overlap is counted twice when in the summation of
        # area_of_a and area_of_b, so we need to subtract it from the
        # total, to get the toal area covered by both the rectangles
        total_area = area_a + area_b - area_of_overlap
        return total_area