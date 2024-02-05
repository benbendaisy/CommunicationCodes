# Definition for a binary tree node.
from collections import Counter
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    """
        Given a binary tree where node values are digits from 1 to 9. A path in the binary tree is said to be pseudo-palindromic if at least one permutation of the node values in the path is a palindrome.

        Return the number of pseudo-palindromic paths going from the root node to leaf nodes.

        Example 1:

        Input: root = [2,3,1,3,1,null,1]
        Output: 2
        Explanation: The figure above represents the given binary tree. There are three paths going from the root node to leaf nodes: the red path [2,3,3], the green path [2,1,1], and the path [2,3,1]. Among these paths only red path and green path are pseudo-palindromic paths since the red path [2,3,3] can be rearranged in [3,2,3] (palindrome) and the green path [2,1,1] can be rearranged in [1,2,1] (palindrome).
        Example 2:

        Input: root = [2,1,1,1,3,null,null,null,null,null,1]
        Output: 1
        Explanation: The figure above represents the given binary tree. There are three paths going from the root node to leaf nodes: the green path [2,1,1], the path [2,1,3,1], and the path [2,1]. Among these paths only the green path is pseudo-palindromic since [2,1,1] can be rearranged in [1,2,1] (palindrome).
        Example 3:

        Input: root = [9]
        Output: 1

        Constraints:

        The number of nodes in the tree is in the range [1, 105].
        1 <= Node.val <= 9
    """
    def pseudoPalindromicPaths1(self, root: Optional[TreeNode]) -> int:
        def checkPseudoPalindromic(arr):
            numDict = Counter(arr)
            oddCnt = 0
            for _, value in numDict.items():
                if value % 2 == 1:
                    oddCnt += 1

                if oddCnt > 1:
                    return False
            return True

        cnt = 0
        def findAllPathes(node: TreeNode, arr):
            nonlocal cnt
            if node is None:
                return
            if node.left is None and node.right is None:
                if checkPseudoPalindromic(arr + [node.val]):
                    cnt += 1
            findAllPathes(node.left, arr + [node.val])
            findAllPathes(node.right, arr + [node.val])

        findAllPathes(root, [])
        return cnt

    def pseudoPalindromicPaths2(self, root: Optional[TreeNode]) -> int:
        def preorder(node, path):
            nonlocal count
            if node:
                # compute occurrences of each digit
                # in the corresponding register
                path = path ^ (1 << node.val)
                # if it's a leaf, check if the path is pseudo-palindromic
                if node.left is None and node.right is None:
                    # check if at most one digit has an odd frequency
                    if path & (path - 1) == 0:
                        count += 1
                else:
                    preorder(node.left, path)
                    preorder(node.right, path)

        count = 0
        preorder(root, 0)
        return count
    
    def pseudoPalindromicPaths(self, root: Optional[TreeNode]) -> int:
        cnt = 0
        def preorder(node, path):
            if not node:
                return
            nonlocal cnt
            # compute occurences of each digit 
            # in the corresponding register
            path = path ^ (1 << node.val)
            # if it's a leaf, check if the path is pseudo-palindromic
            if node.left is None and node.right is None:
                if path & (path - 1) == 0:
                    cnt += 1
            else:
                preorder(node.left, path)
                preorder(node.right, path)
        preorder(root, 0)
        return cnt