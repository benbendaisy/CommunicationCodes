# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    """
    Given two integer arrays, preorder and postorder where preorder is the preorder traversal of a binary tree of distinct values and postorder is the postorder traversal of the same tree, reconstruct and return the binary tree.

    If there exist multiple answers, you can return any of them.

    Example 1:


    Input: preorder = [1,2,4,5,3,6,7], postorder = [4,5,2,6,7,3,1]
    Output: [1,2,3,4,5,6,7]
    Example 2:

    Input: preorder = [1], postorder = [1]
    Output: [1]
    """
    def constructFromPrePost1(self, preorder: List[int], postorder: List[int]) -> Optional[TreeNode]:
        if not preorder or not postorder or len(preorder) != len(postorder):
            return None
        node_dict = {v:i for i, v in enumerate(postorder)}

        def helper(pre_start: int, pre_end: int, post_start: int, post_end: int):
            if pre_start > pre_end:
                return None
            
            node = TreeNode(preorder[pre_start])
            if pre_start == pre_end:
                return node
            
            # Find the index of left child in postorder
            # Left child is the second element in preorder
            left_child_val = preorder[pre_start + 1]
            left_child_post_idx = node_dict[left_child_val]
             # Calculate size of left subtree
            left_subtree_size = left_child_post_idx - post_start + 1

            node.left = helper(pre_start + 1, pre_start + left_subtree_size, post_start, left_child_post_idx)
            node.right = helper(pre_start + left_subtree_size + 1, pre_end, left_child_post_idx + 1, post_end - 1)
            return node
        return helper(0, len(preorder) - 1, 0, len(postorder) - 1)
    
    def constructFromPrePost(self, preorder: List[int], postorder: List[int]) -> Optional[TreeNode]:
        if not preorder or not postorder or len(preorder) != len(postorder):
            return None
        
        node_dict = {v:i for i, v in enumerate(postorder)}

        def helper(pre_start: int, pre_end: int, post_start: int, post_end: int):
            if pre_start > pre_end:
                return None
            
            node = TreeNode(preorder[pre_start])
            if pre_start == pre_end:
                return node
            left_post_idx = node_dict[preorder[pre_start + 1]]
            left_tree_size = left_post_idx - post_start + 1
            node.left = helper(pre_start + 1, pre_start + left_tree_size, post_start, left_post_idx)
            node.right = helper(pre_start + left_tree_size + 1, pre_end, left_post_idx + 1, post_end - 1)
            return node
        
        return helper(0, len(preorder) - 1, 0, len(postorder) - 1)
    