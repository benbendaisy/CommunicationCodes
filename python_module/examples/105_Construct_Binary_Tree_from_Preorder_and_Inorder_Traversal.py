# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
from typing import List, Optional


class Solution:
    def buildTree1(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
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
    
    def buildTree2(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        def helper(pre_arr: List[int], in_arr: List[int]) -> Optional[TreeNode]:
            pos_dict = {v: i for i, v in enumerate(in_arr)}
            if not pre_arr:
                return None
            val = pre_arr[0]
            left_length = pos_dict[val]
            node = TreeNode(val)
            pre_left_arr = pre_arr[1:left_length + 1]
            pre_right_arr = pre_arr[left_length + 1:]

            in_left_arr = in_arr[:left_length]
            in_right_arr = in_arr[left_length + 1:]

            node.left = helper(pre_left_arr, in_left_arr)
            node.right = helper(pre_right_arr, in_right_arr)
            return node
        
        return helper(preorder, inorder)
    
    def buildTree3(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        pos_dict = {v:i for i, v in enumerate(inorder)}
        def helper(pre_s: int, pre_e: int, in_s: int, in_e: int) -> Optional[TreeNode]:
            if pre_s > pre_e or in_s > in_e:
                return None
            
            node = TreeNode(preorder[pre_s])
            pos = pos_dict[preorder[pre_s]]
            left_length = pos - in_s
            node.left = helper(pre_s + 1, pre_s + left_length, in_s, pos - 1)
            node.right = helper(pre_s + left_length + 1, pre_e, pos + 1, in_e)
            return node
        return helper(0, len(preorder) - 1, 0, len(inorder) - 1)

if __name__ == "__main__":
    solution = Solution()
    preorder = [1,2,3]
    inorder = [2,3,1]
    print(solution.buildTree(preorder, inorder))
