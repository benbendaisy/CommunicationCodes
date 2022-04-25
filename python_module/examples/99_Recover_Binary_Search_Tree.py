from typing import Optional, List


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def __init__(self):
        self.nodeMap = {}
        self.arr = []
    def traverseTree(self, root: TreeNode):
        if not root:
            return
        self.traverseTree(root.left)
        self.nodeMap[root.val] = root
        self.arr.append(root.val)
        self.traverseTree(root.right)

    def find_two_swapped(nums: List[int]) -> (int, int):
        n = len(nums)
        x = y = None # Initialize x and y as a value that cannot be the value of a node.
        for i in range(n - 1):
            if nums[i + 1] < nums[i]:
                y = nums[i + 1]
                # first swap occurrence
                if x is None:
                    x = nums[i]
                # second swap occurrence
                else:
                    break
        return x, y

    def recoverTree1(self, root: Optional[TreeNode]) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        self.traverseTree(root)
        def find_two_swapped(nums: List[int]) -> (int, int):
            length = len(nums)
            for i in range(length - 1, 0, -1):
                if nums[i] < nums[i - 1]:
                    j = i - 1
                    while j >=0 and nums[j] > nums[i]:
                        j -= 1
                    return nums[i], nums[j + 1]
        a, b = find_two_swapped(self.arr)

        self.nodeMap[a].val = b
        self.nodeMap[b].val = a

    def recoverTree(self, root: Optional[TreeNode]) -> None:
        if not root:
            return

        stack = []
        cur = root
        prev = x = y = None
        while stack or cur:
            while cur:
                stack.append(cur)
                cur = cur.left
            cur = stack.pop()

            if prev and prev.val > cur.val:
                if not x:
                    x, y = prev, cur
                else:
                    y = cur
                    break

            prev = cur
            cur = cur.right
        x.val, y.val = y.val, x.val
