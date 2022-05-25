# Definition for a binary tree node.
import heapq
from typing import Optional, List


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def __init__(self):
        self.arr = []
    def closestKValues1(self, root: Optional[TreeNode], target: float, k: int) -> List[int]:
        def inOrder(node: Optional[TreeNode]):
            if not node:
                return
            inOrder(node.left)
            self.arr.append(node.val)
            inOrder(node.right)

        inOrder(root)
        res = []
        for i in range(self.arr):
            if len(res) < k:
                res.append(self.arr[i])
            else:
                left = abs(res[0] - target)
                right = abs(res[-1] - target)
                if left > right:
                    if abs(self.arr[i] - target) < left:
                        res.pop(0)
                        res.append(self.arr[i])
                else:
                    if abs(self.arr[i] - target) < right:
                        res.pop()
                        res.append(self.arr[i])
        return res

    def closestKValues2(self, root: Optional[TreeNode], target: float, k: int) -> List[int]:
        def inOrder(node: Optional[TreeNode]):
            if not node:
                return
            inOrder(node.left)
            self.arr.append(node.val)
            inOrder(node.right)

        inOrder(root)
        self.arr.sort(key = lambda x: abs(target - x))
        return self.arr[:k]

    def closestKValues(self, root: Optional[TreeNode], target: float, k: int) -> List[int]:
        heap = []
        def inOrder(node: Optional[TreeNode]):
            if not node:
                return
            inOrder(node.left)
            heapq.heappush(heap, (-abs(node.val - target), node.val))
            if len(heap) > k:
                heapq.heappop(heap)
            inOrder(node.right)

        inOrder(root)
        return [x for _, x in heap]
