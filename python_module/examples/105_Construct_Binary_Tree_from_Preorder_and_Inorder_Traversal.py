# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
from typing import List, Optional


class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        if not preorder or not inorder:
            return None
        indexMap = {v:i for i,v in enumerate(inorder)}

        def constructTree(l1: int, r1: int, l2: int, r2: int):
            if l1 > r1 or l2 > r2:
                return None
            elif l1 == r1 or l2 == r2:
                return TreeNode(preorder[l1])

            node = TreeNode(preorder[l1])
            leftLength = indexMap[preorder[l1]] - l2
            node.left = constructTree(l1 + 1, l1 + leftLength, l2, indexMap[preorder[l1]] - 1)
            node.right = constructTree(l1 + leftLength + 1, r1, indexMap[preorder[l1]] + 1, r2)
            return node

        return constructTree(0, len(preorder) - 1, 0, len(preorder) - 1)

if __name__ == "__main__":
    solution = Solution()
    preorder = [1,2,3]
    inorder = [2,3,1]
    print(solution.buildTree(preorder, inorder))
