from typing import List


class Solution:
    """
    Given an integer rowIndex, return the rowIndexth (0-indexed) row of the Pascal's triangle.

    In Pascal's triangle, each number is the sum of the two numbers directly above it as shown:

    Example 1:

    Input: rowIndex = 3
    Output: [1,3,3,1]
    Example 2:

    Input: rowIndex = 0
    Output: [1]
    Example 3:

    Input: rowIndex = 1
    Output: [1,1]
    """
    def getRow(self, rowIndex: int) -> List[int]:
        @cache
        def get_num(row, col):
            if row == 0 or col == 0 or row == col:
                return 1
            return get_num(row - 1, col - 1) + get_num(row - 1, col)
        ans = []
        for i in range(rowIndex + 1):
            ans.append(get_num(rowIndex, i))
        return ans