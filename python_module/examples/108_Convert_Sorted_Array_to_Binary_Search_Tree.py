# Definition for a binary tree node.
from typing import List, Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    """
        Given an integer array nums where the elements are sorted in ascending order, convert it to a height-balanced binary search tree.

        A height-balanced binary tree is a binary tree in which the depth of the two subtrees of every node never differs by more than one.

        Example 1:

        Input: nums = [-10,-3,0,5,9]
        Output: [0,-3,9,-10,null,5]
        Explanation: [0,-10,5,null,-3,null,9] is also accepted:

        Example 2:

        Input: nums = [1,3]
        Output: [3,1]
        Explanation: [1,null,3] and [3,1] are both height-balanced BSTs.

        Constraints:

        1 <= nums.length <= 104
        -104 <= nums[i] <= 104
        nums is sorted in a strictly increasing order.
    """
    def sortedArrayToBST1(self, nums: List[int]) -> Optional[TreeNode]:
        if not nums:
            return None
        def constructBinaryTree(left, right):
            if left == right:
                return TreeNode(nums[left])
            elif left + 1 == right:
                leftNode = TreeNode(nums[left])
                rightNode = TreeNode(nums[right])
                leftNode.right = rightNode
                return leftNode

            mid = left + (right - left) // 2
            node = TreeNode(nums[mid])
            node.left = constructBinaryTree(left, mid - 1)
            node.right = constructBinaryTree(mid + 1, right)
            return node

        return constructBinaryTree(0, len(nums) - 1)
    
    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:
        def helper(arr: list) -> TreeNode:
            if not arr:
                return None
            
            mid = len(arr) // 2
            node = TreeNode(arr[mid])
            node.left = helper(arr[:mid])
            node.right = helper(arr[mid + 1:])
            return node
        return helper(nums)
