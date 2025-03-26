class Solution:
    """
    You are given an integer n representing the dimensions of an n x n grid, with the origin at the bottom-left corner of the grid. You are also given a 2D array of coordinates rectangles, where rectangles[i] is in the form [startx, starty, endx, endy], representing a rectangle on the grid. Each rectangle is defined as follows:

    (startx, starty): The bottom-left corner of the rectangle.
    (endx, endy): The top-right corner of the rectangle.
    Note that the rectangles do not overlap. Your task is to determine if it is possible to make either two horizontal or two vertical cuts on the grid such that:

    Each of the three resulting sections formed by the cuts contains at least one rectangle.
    Every rectangle belongs to exactly one section.
    Return true if such cuts can be made; otherwise, return false.

    Example 1:

    Input: n = 5, rectangles = [[1,0,5,2],[0,2,2,4],[3,2,5,3],[0,4,4,5]]

    Output: true

    Explanation:

    The grid is shown in the diagram. We can make horizontal cuts at y = 2 and y = 4. Hence, output is true.

    Example 2:

    Input: n = 4, rectangles = [[0,0,1,1],[2,0,3,4],[0,2,2,3],[3,0,4,3]]

    Output: true

    Explanation:

    We can make vertical cuts at x = 2 and x = 3. Hence, output is true.

    Example 3:

    Input: n = 4, rectangles = [[0,2,2,4],[1,0,3,2],[2,2,3,4],[3,0,4,2],[3,2,4,4]]

    Output: false

    Explanation:

    We cannot make two horizontal or two vertical cuts that satisfy the conditions. Hence, output is false.
    """
    def checkValidCuts1(self, n: int, rectangles: List[List[int]]) -> bool:
        def can_split(intervals: List[List[int]]) -> bool:
            intervals.sort()
            cuts = 0
            current_end = intervals[0][1]
            
            for start, end in intervals[1:]:
                if start >= current_end:
                    cuts += 1
                    if cuts >= 2:
                        return True
                current_end = max(current_end, end)
            
            return False

        x_intervals = [[x1, x2] for x1, _, x2, _ in rectangles]
        y_intervals = [[y1, y2] for _, y1, _, y2 in rectangles]

        return can_split(x_intervals) or can_split(y_intervals)
    
    def checkValidCuts2(self, n: int, rectangles: List[List[int]]) -> bool:
        x_intervals = [[x1, x2] for x1, _, x2, _ in rectangles]
        y_intervals = [[y1, y2] for _, y1, _, y2 in rectangles]

        def is_valid(intervals: list) -> bool:
            intervals.sort()
            cur_end = intervals[0][1]
            cuts = 0
            for start, end in intervals[1:]:
                if start >= cur_end:
                    cuts += 1
                    if cuts >= 2:
                        return True
                cur_end = max(cur_end, end)
            
            return False
        
        return is_valid(x_intervals) or is_valid(y_intervals)