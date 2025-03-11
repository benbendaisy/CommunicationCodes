# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    """
    Given the root of a binary tree, return the length of the longest path, where each node in the path has the same value. This path may or may not pass through the root.

    The length of the path between two nodes is represented by the number of edges between them.

    Example 1:

    Input: root = [5,4,5,1,1,null,5]
    Output: 2
    Explanation: The shown image shows that the longest path of the same value (i.e. 5).
    Example 2:

    Input: root = [1,4,5,4,4,null,5]
    Output: 2
    Explanation: The shown image shows that the longest path of the same value (i.e. 4).
    """
    def longestUnivaluePath(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        self.max_dist = 0
        def helper(node: TreeNode):
            if not node:
                return 0
            left_path = helper(node.left)
            right_path = helper(node.right)
            left = left_path + 1 if node.left and node.left.val == node.val else 0
            right = right_path + 1 if node.right and node.right.val == node.val else 0
             # Update max path (left + right) from this node
            self.max_dist = max(self.max_dist, left + right)
            # Return the longest single path extending downward
            return max(left, right)
        helper(root)
        return self.max_dist