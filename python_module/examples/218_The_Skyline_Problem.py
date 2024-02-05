import heapq
from typing import List


# Define the disjoint-set structure.
class UnionFind():
    def __init__(self, N):
        self.root = list(range(N))
    def find(self, x):
        if self.root[x] != x:
            self.root[x] = self.find(self.root[x])
        return self.root[x]
    def union(self, x, y):
        self.root[x] = self.root[y]

class Solution:
    """
        A city's skyline is the outer contour of the silhouette formed by all the buildings in that city when viewed from a distance. Given the locations and heights of all the buildings, return the skyline formed by these buildings collectively.

        The geometric information of each building is given in the array buildings where buildings[i] = [lefti, righti, heighti]:

        lefti is the x coordinate of the left edge of the ith building.
        righti is the x coordinate of the right edge of the ith building.
        heighti is the height of the ith building.
        You may assume all buildings are perfect rectangles grounded on an absolutely flat surface at height 0.

        The skyline should be represented as a list of "key points" sorted by their x-coordinate in the form [[x1,y1],[x2,y2],...]. Each key point is the left endpoint of some horizontal segment in the skyline except the last point in the list, which always has a y-coordinate 0 and is used to mark the skyline's termination where the rightmost building ends. Any ground between the leftmost and rightmost buildings should be part of the skyline's contour.

        Note: There must be no consecutive horizontal lines of equal height in the output skyline. For instance, [...,[2 3],[4 5],[7 5],[11 5],[12 7],...] is not acceptable; the three lines of height 5 should be merged into one in the final output as such: [...,[2 3],[4 5],[12 7],...]

        Example 1:

        Input: buildings = [[2,9,10],[3,7,15],[5,12,12],[15,20,10],[19,24,8]]
        Output: [[2,10],[3,15],[7,12],[12,0],[15,10],[20,8],[24,0]]
        Explanation:
        Figure A shows the buildings of the input.
        Figure B shows the skyline formed by those buildings. The red points in figure B represent the key points in the output list.
        Example 2:

        Input: buildings = [[0,2,3],[2,5,3]]
        Output: [[0,3],[5,0]]

        Constraints:

        1 <= buildings.length <= 104
        0 <= lefti < righti <= 231 - 1
        1 <= heighti <= 231 - 1
        buildings is sorted by lefti in non-decreasing order.
    """
    def getSkyline1(self, buildings: List[List[int]]) -> List[List[int]]:
        # Sort the unique positions of all the edges.
        positions = sorted(list(set([x for building in buildings for x in building[:2]])))

        # Hast table 'edge_index_map' to record every {position : index} pairs in edges.
        edge_index_map = {x:i for i, x in enumerate(positions)}
        heights = [0] * len(edge_index_map)
        for left, right, height in buildings:
            left_index = edge_index_map[left]
            right_index = edge_index_map[right]

            # Update the maximum height within the range [left_idx, right_idx)
            for i in range(left_index, right_index):
                heights[i] = max(heights[i], height)
        ans = []
        for i in range(len(heights)):
            height = heights[i]
            position = positions[i]
            if not ans or ans[-1][1] != height:
                ans.append([position, height])
        return ans

    def getSkyline2(self, buildings: List[List[int]]) -> List[List[int]]:
        positions = sorted(list(set([x for building in buildings for x in building[:2]])))

        # 'answer' for skyline key points
        ans = []
        # For each position, draw an imaginary vertical line.
        for position in positions:
            # current max height
            maxHeight = 0

            # iterate over all buildings
            for left, right, height in buildings:
                # update maxHeight if necessary
                if left <= position < right:
                    maxHeight = max(maxHeight, height)

            # If its the first key point or the height changes,
            # we add [position, max_height] to 'answer'.
            if not ans or ans[-1][1] != maxHeight:
                ans.append([position, maxHeight])
        return ans

    def getSkyline3(self, buildings: List[List[int]]) -> List[List[int]]:
        # Sort the unique positions of all the edges.
        edges = sorted(list(set([x for building in buildings for x in building[:2]])))
        # Hast table 'edge_index_map' record every {position : index} pairs in 'edges'.
        edgeIdxMap = {x: idx for idx, x in enumerate(edges)}
        # Sort buildings by descending order of heights.
        buildings.sort(key=lambda x: -x[2])
        n = len(edges)
        edgeUF = UnionFind(n)
        heights = [0] * n
        # Iterate over all the buildings by descending height.
        for left, right, height in buildings:
            leftIdx, rightIdx = edgeIdxMap[left], edgeIdxMap[right]
            # While we haven't update the the root of 'left_idx':
            while leftIdx < rightIdx:
                # Find the root of left index 'left_idx', that is:
                # The rightmost index having the same height as 'left_idx'.
                leftIdx = edgeUF.find(leftIdx)

                # If left_idx < right_idx, we have to update both the root and height
                # of left_idx, and move on to the next index towards right_idx.
                # That is: increment left_idx by 1.
                if leftIdx < rightIdx:
                    edgeUF.union(leftIdx, rightIdx)
                    heights[leftIdx] = height
                    leftIdx += 1
        # Finally, we just need to iterate over updated heights, and
        # add every skyline key point to 'answer'.
        ans = []
        for i in range(n):
            if i == 0 or heights[i] != heights[i - 1]:
                ans.append([edges[i], heights[i]])
        return ans

    def getSkyline(self, buildings: List[List[int]]) -> List[List[int]]:
        # Iterate over all buildings, for each building i,
        # add (position, i) to edges.
        edges = []
        for i, build in enumerate(buildings):
            edges.append([build[0], i])
            edges.append([build[1], i])

        # Sort edges by non-decreasing order.
        edges.sort()

        # Initailize an empty Priority Queue 'live' to store all the
        # newly added buildings, an empty list answer to store the skyline key points.
        live, answer = [], []
        idx = 0

        # Iterate over all the sorted edges.
        while idx < len(edges):

            # Since we might have multiple edges at same x,
            # Let the 'curr_x' be the current position.
            curr_x = edges[idx][0]

            # While we are handling the edges at 'curr_x':
            while idx < len(edges) and edges[idx][0] == curr_x:
                # The index 'b' of this building in 'buildings'
                b = edges[idx][1]

                # If this is a left edge of building 'b', we
                # add (height, right) of building 'b' to 'live'.
                if buildings[b][0] == curr_x:
                    right = buildings[b][1]
                    height = buildings[b][2]
                    heapq.heappush(live, [-height, right])

                # If the tallest live building has been passed,
                # we remove it from 'live'.
                while live and live[0][1] <= curr_x:
                    heapq.heappop(live)
                idx += 1

            # Get the maximum height from 'live'.
            max_height = -live[0][0] if live else 0

            # If the height changes at this curr_x, we add this
            # skyline key point [curr_x, max_height] to 'answer'.
            if not answer or max_height != answer[-1][1]:
                answer.append([curr_x, max_height])

        # Return 'answer' as the skyline.
        return answer

