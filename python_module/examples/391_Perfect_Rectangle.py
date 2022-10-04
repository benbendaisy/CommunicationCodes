from typing import List


class Solution:
    """
        Given an array rectangles where rectangles[i] = [xi, yi, ai, bi] represents an axis-aligned rectangle. The bottom-left point of the rectangle is (xi, yi) and the top-right point of it is (ai, bi).

        Return true if all the rectangles together form an exact cover of a rectangular region.

        Example 1:

        Input: rectangles = [[1,1,3,3],[3,1,4,2],[3,2,4,4],[1,3,2,4],[2,3,3,4]]
        Output: true
        Explanation: All 5 rectangles together form an exact cover of a rectangular region.
        Example 2:

        Input: rectangles = [[1,1,2,3],[1,3,2,4],[3,1,4,2],[3,2,4,4]]
        Output: false
        Explanation: Because there is a gap between the two rectangular regions.
        Example 3:

        Input: rectangles = [[1,1,3,3],[3,1,4,2],[1,3,2,4],[2,2,4,4]]
        Output: false
        Explanation: Because two of the rectangles overlap with each other.

        Constraints:

        1 <= rectangles.length <= 2 * 104
        rectangles[i].length == 4
        -105 <= xi, yi, ai, bi <= 105
    """
    def isRectangleCover(self, rectangles: List[List[int]]) -> bool:
        """
        We need to check two things:

            the external corners must appear only once, and the ones inside have to be an even number (we filter them with xor).
            the total area of all the rectangles together, has to be equal to the area created by the external corners
        :param rectangles:
        :return:
        """
        area = 0
        corners = set()
        a = lambda: (Y - y) * (X - x)

        for x, y, X, Y in rectangles:
            area += a()
            corners ^= {(x, y), (x, Y), (X, y), (X, Y)}

        if len(corners) != 4:
            return False
        x, y = min(corners, key=lambda x: x[0] + x[1])
        X, Y = max(corners, key=lambda x: x[0] + x[1])

        return a() == area
