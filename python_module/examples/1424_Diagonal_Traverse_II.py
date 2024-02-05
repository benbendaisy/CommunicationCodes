from typing import List


class Solution:
    """
    Given a 2D integer array nums, return all elements of nums in diagonal order as shown in the below images.

    Example 1:

    Input: nums = [[1,2,3],[4,5,6],[7,8,9]]
    Output: [1,4,2,7,5,3,8,6,9]
    Example 2:

    Input: nums = [[1,2,3,4,5],[6,7],[8],[9,10,11],[12,13,14,15,16]]
    Output: [1,6,2,8,7,3,9,4,12,10,5,13,11,14,15,16]
    """
    def findDiagonalOrder1(self, nums: List[List[int]]) -> List[int]:
        groups = defaultdict(list)
        m = len(nums)
        for row in range(m - 1, -1, -1):
            for col in range(len(nums[row])):
                diagonal = row + col
                groups[diagonal].append(nums[row][col])
        res = []
        cur = 0
        while cur in groups:
            res.extend(groups[cur])
            cur += 1
        return res
    
    def findDiagonalOrder(self, nums: List[List[int]]) -> List[int]:
        que = deque([(0, 0)])
        res = []
        m = len(nums)
        while que:
            row, col = que.popleft()
            res.append(nums[row][col])
            if col == 0 and row + 1 < m:
                que.append((row + 1, col))
            if col + 1 < len(nums[row]):
                que.append((row, col + 1))
        return res