from typing import List


class Solution:
    """
        You are given an array trees where trees[i] = [xi, yi] represents the location of a tree in the garden.

        You are asked to fence the entire garden using the minimum length of rope as it is expensive. The garden is well fenced only if all the trees are enclosed.

        Return the coordinates of trees that are exactly located on the fence perimeter.

        Example 1:

        Input: points = [[1,1],[2,2],[2,0],[2,4],[3,3],[4,2]]
        Output: [[1,1],[2,0],[3,3],[2,4],[4,2]]
        Example 2:

        Input: points = [[1,2],[2,2],[4,2]]
        Output: [[4,2],[2,2],[1,2]]
    """
    def outerTrees(self, trees: List[List[int]]) -> List[List[int]]:
        def compare_slope(p1, p2, p3):
            x1, y1 = p1
            x2, y2 = p2
            x3, y3 = p3
            """
            slope of p1 and p2 will be y2-y1/x2-x1
            slope of p2 and p3 will be y3-y2/x3-x2
            combining them both gives
            y3-y2/x3-x2   -   y2-y1/x2-x1 
            this eqn represents the resultant formed by those two
            if this is greater than 0 then direction will be counter clockwise else clockwise
            """
            return (y3 - y2) * (x2 - x1) - (y2 - y1) * (x3 - x2) # return <0 if clockwise
        upper, lower = [], []
        for point in sorted(trees):
            while len(lower) >= 2 and compare_slope(lower[-2], lower[-1], point) < 0: lower.pop()
            while len(upper) >= 2 and compare_slope(upper[-2], upper[-1], point) > 0: upper.pop()
            lower.append(tuple(point))
            upper.append(tuple(point))
        return list(set(lower + upper))