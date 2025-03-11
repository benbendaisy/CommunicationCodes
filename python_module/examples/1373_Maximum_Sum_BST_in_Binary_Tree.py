# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    """
    Given a binary tree root, return the maximum sum of all keys of any sub-tree which is also a Binary Search Tree (BST).

    Assume a BST is defined as follows:

    The left subtree of a node contains only nodes with keys less than the node's key.
    The right subtree of a node contains only nodes with keys greater than the node's key.
    Both the left and right subtrees must also be binary search trees.
    
    Example 1:

    Input: root = [1,4,3,2,4,2,5,null,null,null,null,null,null,4,6]
    Output: 20
    Explanation: Maximum sum in a valid Binary search tree is obtained in root node with key equal to 3.
    Example 2:



    Input: root = [4,3,null,1,2]
    Output: 2
    Explanation: Maximum sum in a valid Binary search tree is obtained in a single root node with key equal to 2.
    Example 3:

    Input: root = [-4,-2,-5]
    Output: 0
    Explanation: All values are negatives. Return an empty BST.
    """
    def maxSumBST1(self, root: Optional[TreeNode]) -> int:
        self.max_sum = 0  # Track the maximum sum of a valid BST

        def helper(node: Optional[TreeNode]) -> tuple:
            """
            Returns a tuple (is_bst, min_val, max_val, sum):
            - is_bst: Whether the subtree rooted at `node` is a BST.
            - min_val: The minimum value in the subtree.
            - max_val: The maximum value in the subtree.
            - sum: The sum of the subtree if it's a BST, otherwise 0.
            """
            if not node:
                return (True, float('inf'), float('-inf'), 0)  # Empty tree is a BST

            # Recursively check left and right subtrees
            left_is_bst, left_min, left_max, left_sum = helper(node.left)
            right_is_bst, right_min, right_max, right_sum = helper(node.right)

            # Check if the current subtree is a BST
            is_bst = (
                left_is_bst and right_is_bst and  # Both subtrees must be BSTs
                left_max < node.val < right_min  # Current node's value must be in the valid range
            )

            # Calculate the sum of the current subtree if it's a BST
            if is_bst:
                subtree_sum = left_sum + node.val + right_sum
                self.max_sum = max(self.max_sum, subtree_sum)  # Update the maximum sum
                return (True, min(left_min, node.val), max(right_max, node.val), subtree_sum)
            else:
                # If not a BST, return 0 for the sum
                return (False, 0, 0, 0)

        helper(root)  # Start the recursion
        return self.max_sum

    def maxSumBST(self, root: Optional[TreeNode]) -> int:
        self.max_sum = 0  # Track the maximum sum of a valid BST

        def helper(node: Optional[TreeNode]) -> tuple:
            if not node:
                return (True, float('inf'), float('-inf'), 0)
            
            left_is_bst, left_min, left_max, left_sum = helper(node.left)
            right_is_bst, right_min, right_max, right_sum = helper(node.right)
            is_bst = left_is_bst and right_is_bst and left_max < node.val < right_min

            if is_bst:
                sub_sum = left_sum + right_sum + node.val
                self.max_sum = max(self.max_sum, sub_sum)
                return (True, min(left_min, node.val), max(right_max, node.val), sub_sum)
            else:
                return (False, node.val, node.val, node.val)
        
        helper(root)
        return self.max_sum