# Definition for singly-linked list.
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    """
    Given the head of a singly linked list where elements are sorted in ascending order, convert it to a
    height-balanced
    binary search tree

    Example 1:

    Input: head = [-10,-3,0,5,9]
    Output: [0,-3,9,-10,null,5]
    Explanation: One possible answer is [0,-3,9,-10,null,5], which represents the shown height balanced BST.
    Example 2:

    Input: head = []
    Output: []
    """
    def sortedListToBST(self, head: Optional[ListNode]) -> Optional[TreeNode]:
        def construct_BST(left: ListNode, right: ListNode):
            if left == right:
                return None
            slow, fast = left, left
            while fast != right and fast.next != right:
                slow = slow.next
                fast = fast.next.next
            root = TreeNode(slow.val)
            root.left = construct_BST(left, slow)
            root.right = construct_BST(slow.next, right)
            return root

        if not head:
            return None
        if not head.next:
            root = TreeNode(head.val)
            return root
        return construct_BST(head, None)

