class Solution:
    """
    Given an m x n matrix mat, return an array of all the elements of the array in a diagonal order.

    Example 1:

    Input: mat = [[1,2,3],[4,5,6],[7,8,9]]
    Output: [1,2,4,7,5,3,6,8,9]
    Example 2:

    Input: mat = [[1,2],[3,4]]
    Output: [1,2,3,4]
    """
    def findDiagonalOrder(self, mat: List[List[int]]) -> List[int]:
        if not mat or not mat[0]:
            return []
        rows, cols = len(mat), len(mat[0])
        zig_dict = defaultdict(list)
        for i in range(rows):
            for j in range(cols):
                zig_dict[i + j].append(mat[i][j])
        res = []
        for key, value in zig_dict.items():
            if key % 2 == 0:
                [res.append(x) for x in value[::-1]]
            else:
                [res.append(x) for x in value]
        return res