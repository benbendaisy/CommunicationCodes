# Definition for a binary tree node.
from collections import deque
from typing import Optional, List


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    """
        Given the root of a binary tree, return the zigzag level order traversal of its nodes' values. (i.e., from left to right, then right to left for the next level and alternate between).

        Example 1:

        Input: root = [3,9,20,null,null,15,7]
        Output: [[3],[20,9],[15,7]]
        Example 2:

        Input: root = [1]
        Output: [[1]]
        Example 3:

        Input: root = []
        Output: []
    """
    def zigzagLevelOrder1(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []

        que = deque([root])
        res, direction = [], 1
        while que:
            level = [node.val for node in que]
            if direction == -1:
                level.reverse()
            res.append(level)
            direction *= -1

            for i in range(len(que)):
                node = que.popleft()
                if node.left:
                    que.append(node.left)
                if node.right:
                    que.append(node.right)
        return res
    
    def zigzagLevelOrder2(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []
        pos_dict = defaultdict(list)
        def helper(node: TreeNode, dep: int):
            if not node:
                return
            
            pos_dict[dep].append(node.val)
            helper(node.left, dep + 1)
            helper(node.right, dep + 1)
                
        helper(root, 0)
        res = []
        for key, level in pos_dict.items():
            if key % 2 == 0:
                res.append(level)
            else:
                res.append(level[::-1])

        return res
    
    def zigzagLevelOrder3(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []
        que = deque([root])
        res, dep = [], 0
        while que:
            arr, length = [], len(que)
            for _ in range(length):
                node = que.popleft()
                arr.append(node.val)
                if node.left:
                    que.append(node.left)
                if node.right:
                    que.append(node.right)
            if dep % 2 == 0:
                res.append(arr)
            else:
                res.append(arr[::-1])
            dep += 1
        return res
