# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    """
    You are given the root of a binary tree with the following properties:

    Leaf nodes have either the value 0 or 1, representing false and true respectively.
    Non-leaf nodes have either the value 2, 3, 4, or 5, representing the boolean operations OR, AND, XOR, and NOT, respectively.
    You are also given a boolean result, which is the desired result of the evaluation of the root node.

    The evaluation of a node is as follows:

    If the node is a leaf node, the evaluation is the value of the node, i.e. true or false.
    Otherwise, evaluate the node's children and apply the boolean operation of its value with the children's evaluations.
    In one operation, you can flip a leaf node, which causes a false node to become true, and a true node to become false.

    Return the minimum number of operations that need to be performed such that the evaluation of root yields result. It can be shown that there is always a way to achieve result.

    A leaf node is a node that has zero children.

    Note: NOT nodes have either a left child or a right child, but other non-leaf nodes have both a left child and a right child.

    Example 1:

    Input: root = [3,5,4,2,null,1,1,1,0], result = true
    Output: 2
    Explanation:
    It can be shown that a minimum of 2 nodes have to be flipped to make the root of the tree
    evaluate to true. One way to achieve this is shown in the diagram above.
    Example 2:

    Input: root = [0], result = false
    Output: 0
    Explanation:
    The root of the tree already evaluates to false, so 0 nodes have to be flipped.
    """
    def minimumFlips1(self, root: Optional[TreeNode], result: bool) -> int:
        def helper(node):
            if node.val == 0: return {True:1, False:0}
            if node.val == 1: return {True:0, False:1}
            left = helper(node.left) if node.left else None
            right = helper(node.right) if node.right else None
            res={}
            
            if node.val == 5:
                if not left:
                    res[True], res[False] = right[False], right[True]
                else:
                    res[True], res[False] = left[False], left[True]
                    
            elif node.val == 4:
                res[True] = min(left[True] + right[False], left[False] + right[True])
                res[False] = min(left[True] + right[True], left[False] + right[False])
                
            elif node.val == 3:
                res[True] = left[True] + right[True]
                res[False] = min(left[True] + right[False], left[False] + right[True], left[False] + right[False])
            
            elif node.val == 2:
                res[True] = min(left[True] + right[False], left[False] + right[True], left[True] + right[True])
                res[False] = left[False] + right[False]
                
            return res
        
        return helper(root)[result]
    
    def minimumFlips2(self, root: Optional[TreeNode], result: bool) -> int:
        @cache
        def dfs(node, target):
            if not node:
                return float('inf')
            
            if not node.left and not node.right:  # Leaf node
                return int(node.val != target)
            
            if node.val == 5:  # NOT operation
                return dfs(node.left or node.right, not target)
            
            left_true = dfs(node.left, True)
            left_false = dfs(node.left, False)
            right_true = dfs(node.right, True) if node.right else float('inf')
            right_false = dfs(node.right, False) if node.right else float('inf')
            
            if node.val == 2:  # OR operation
                if target:
                    return min(left_true, right_true)
                else:
                    return left_false + right_false
            elif node.val == 3:  # AND operation
                if target:
                    return left_true + right_true
                else:
                    return min(left_false, right_false)
            elif node.val == 4:  # XOR operation
                if target:
                    return min(left_true + right_false, left_false + right_true)
                else:
                    return min(left_true + right_true, left_false + right_false)
            
            return float('inf')
        
        return dfs(root, result)
    
    def minimumFlips(self, root: Optional[TreeNode], result: bool) -> int:
        if not root:
            return -1
        
        @cache
        def helper(node: TreeNode, target: bool):
            if not node.left and not node.right:
                return int(node.val != target)
            if node.val == 5:
                return helper(node.left or node.right, not target)
            
            left_true = helper(node.left, True)
            left_false = helper(node.left, False)
            right_true = helper(node.right, True)
            right_false = helper(node.right, False)

            match node.val:
                case 2:
                    if target:
                        return min(left_true, right_true)
                    else:
                        return left_false + right_false
                case 3:
                    if target:
                        return left_true + right_true
                    else:
                        return min(left_false, right_false)
                case 4:
                    if target:
                        return min(left_true + right_false, left_false + right_true)
                    else:
                        return min(left_true + right_true, left_false + right_false)
            return float('inf')
        return helper(root, result)