from typing import List


class Solution:
    """
        On a 2D plane, we place n stones at some integer coordinate points. Each coordinate point may have at most one stone.

        A stone can be removed if it shares either the same row or the same column as another stone that has not been removed.

        Given an array stones of length n where stones[i] = [xi, yi] represents the location of the ith stone, return the largest possible number of stones that can be removed.


        Example 1:

        Input: stones = [[0,0],[0,1],[1,0],[1,2],[2,1],[2,2]]
        Output: 5
        Explanation: One way to remove 5 stones is as follows:
        1. Remove stone [2,2] because it shares the same row as [2,1].
        2. Remove stone [2,1] because it shares the same column as [0,1].
        3. Remove stone [1,2] because it shares the same row as [1,0].
        4. Remove stone [1,0] because it shares the same column as [0,0].
        5. Remove stone [0,1] because it shares the same row as [0,0].
        Stone [0,0] cannot be removed since it does not share a row/column with another stone still on the plane.
        Example 2:

        Input: stones = [[0,0],[0,2],[1,1],[2,0],[2,2]]
        Output: 3
        Explanation: One way to make 3 moves is as follows:
        1. Remove stone [2,2] because it shares the same row as [2,0].
        2. Remove stone [2,0] because it shares the same column as [0,0].
        3. Remove stone [0,2] because it shares the same row as [0,0].
        Stones [0,0] and [1,1] cannot be removed since they do not share a row/column with another stone still on the plane.
        Example 3:

        Input: stones = [[0,0]]
        Output: 0
        Explanation: [0,0] is the only stone on the plane, so you cannot remove it.
    """
    def __init__(self):
        self.parent = {}
        self.size_dict = {}
    def removeStones(self, stones: List[List[int]]) -> int:
        n = len(stones)
        def share_same_row_or_column(x1, y1, x2, y2):
            """
            Return true if stone a and b shares row or column
            :param x1:
            :param y1:
            :param x2:
            :param y2:
            :return:
            """
            return  x1 == x2 or y1 == y2

        def find(x):
            """
            Returns the representative of vertex x
            :param parent:
            :param x:
            :return:
            """
            if x == self.parent[x]:
                return x
            return find(self.parent[x])

        def perform_union(x, y):
            """
            Combine the stone x and y, and returns 1 if they were not connected
            :param x:
            :param y:
            :return:
            """
            x = find(x)
            y = find(y)
            if x == y:
                return 0
            elif self.size_dict[x] > self.size_dict[y]:
                self.parent[y] = x
                self.size_dict[x] += self.size_dict[y]
            else:
                self.parent[x] = y
                self.size_dict[y] += self.size_dict[x]
            return 1

        # Initialize parent to itself and size as 1
        for i in range(n):
            self.parent[i] = i
            self.size_dict[i] = 1
        component_cnt = n
        for i in range(n):
            for j in range(i + 1, n):
                if share_same_row_or_column(stones[i][0], stones[i][1], stones[j][0], stones[j][1]):
                    # Decrement the components if union involved merging
                    component_cnt -= perform_union(i, j)
        return n - component_cnt
