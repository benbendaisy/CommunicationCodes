class Solution:
    """
    You are given several boxes with different colors represented by different positive numbers.

    You may experience several rounds to remove boxes until there is no box left. Each time you can choose some continuous boxes with the same color (i.e., composed of k boxes, k >= 1), remove them and get k * k points.

    Return the maximum points you can get.

    Example 1:

    Input: boxes = [1,3,2,2,2,3,4,3,1]
    Output: 23
    Explanation:
    [1, 3, 2, 2, 2, 3, 4, 3, 1] 
    ----> [1, 3, 3, 4, 3, 1] (3*3=9 points) 
    ----> [1, 3, 3, 3, 1] (1*1=1 points) 
    ----> [1, 1] (3*3=9 points) 
    ----> [] (2*2=4 points)
    Example 2:

    Input: boxes = [1,1,1]
    Output: 9
    Example 3:

    Input: boxes = [1]
    Output: 1
    """
    def removeBoxes(self, boxes: List[int]) -> int:
        if not boxes:
            return 0
        
        @cache
        def helper(path: tuple) -> int:
            if not path:
                return 0
            
            max_point = float('-inf')
            n = len(path)
            i = 0
            while i < n:
                k, j = 1, i + 1
                while j < n and path[i] == path[j]:
                    j += 1
                    k += 1
                max_point = max(max_point, k * k + helper(path[:i] + path[j:]))
                i = j
            return max_point
        return helper(tuple(boxes))