# Definition for a binary tree node.
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    """
        Given a root node reference of a BST and a key, delete the node with the given key in the BST. Return the root node reference (possibly updated) of the BST.

        Basically, the deletion can be divided into two stages:

        Search for a node to remove.
        If the node is found, delete the node.

        Example 1:

        Input: root = [5,3,6,2,4,null,7], key = 3
        Output: [5,4,6,2,null,null,7]
        Explanation: Given key to delete is 3. So we find the node with value 3 and delete it.
        One valid answer is [5,4,6,2,null,null,7], shown in the above BST.
        Please notice that another valid answer is [5,2,6,null,4,null,7] and it's also accepted.

        Example 2:

        Input: root = [5,3,6,2,4,null,7], key = 0
        Output: [5,3,6,2,4,null,7]
        Explanation: The tree does not contain a node with value = 0.
        Example 3:

        Input: root = [], key = 0
        Output: []
    """
    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
        # If the root is None, return None
        if not root:
            return None

        # If the key to be deleted is less than the root's key,
        # then the function is recursively called with the left subtree
        if key < root.val:
            root.left = self.deleteNode(root.left, key)

        # If the key to be deleted is greater than the root's key,
        # then the function is recursively called with the right subtree
        elif key > root.val:
            root.right = self.deleteNode(root.right, key)
        else:
            # If the root has no child or only one child, then the root is replaced with its child
            if not root.left:
                return root.right
            elif not root.right:
                return root.left
            # If the root has two children, then the inorder successor of the root is found
            else:
                node = root.right
                while node.left:
                    node = node.left
                # The value of the inorder successor is copied to the root
                root.val = node.val
                # The inorder successor is then deleted from the right subtree of the root
                root.right = self.deleteNode(root.right, node.val)
        return root

