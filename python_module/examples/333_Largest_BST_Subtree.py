# Definition for a binary tree node.
import math
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    """
        Given the root of a binary tree, find the largest subtree, which is also a Binary Search Tree (BST), where the largest means subtree has the largest number of nodes.

        A Binary Search Tree (BST) is a tree in which all the nodes follow the below-mentioned properties:

        The left subtree values are less than the value of their parent (root) node's value.
        The right subtree values are greater than the value of their parent (root) node's value.
        Note: A subtree must include all of its descendants.

        Example 1:

        Input: root = [10,5,15,1,8,null,7]
        Output: 3
        Explanation: The Largest BST Subtree in this case is the highlighted one. The return value is the subtree's size, which is 3.
        Example 2:

        Input: root = [4,2,7,2,3,5,null,2,null,null,null,null,null,1]
        Output: 2

        Constraints:

        The number of nodes in the tree is in the range [0, 104].
        -104 <= Node.val <= 104
    """
    def largestBSTSubtree(self, root: Optional[TreeNode]) -> int:
        def check(node, lb, ub):
            """
            check if current tree is a valid binary search tree
            :param node:
            :param lb:
            :param ub:
            :return:
            """
            if not node:
                return True
            if node.val <= lb or node.val >= ub:
                return False
            return check(node.left, lb, node.val) and check(node.right, node.val, ub)

        def countNodes(node):
            """
            count the num of nodes those are BST
            :param node:
            :return:
            """
            if not node:
                return 0
            return 1 + countNodes(node.left) + countNodes(node.right)

        def largestBSTSubtree(node):
            """
            calculate the largest BST subtree
            :param node:
            :return:
            """
            if not node:
                return 0
            if check(node, -math.inf, math.inf):
                return countNodes(node)
            return max(largestBSTSubtree(node.left), largestBSTSubtree(node.right))

        return largestBSTSubtree(root)

