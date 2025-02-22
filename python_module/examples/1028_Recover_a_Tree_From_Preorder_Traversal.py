# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def recoverFromPreorder1(self, traversal: str) -> Optional[TreeNode]:
        stack = []  # Stack to maintain ancestors
        i = 0  # Pointer to traverse the input string

        while i < len(traversal):
            depth = 0  # Count dashes
            while i < len(traversal) and traversal[i] == '-':
                depth += 1
                i += 1
            
            value = 0  # Extract node value
            while i < len(traversal) and traversal[i].isdigit():
                value = value * 10 + int(traversal[i])
                i += 1
            
            node = TreeNode(value)  # Create new TreeNode

            if depth == len(stack):  # Left child case
                if stack:
                    stack[-1].left = node
            else:  # Right child case, pop until reaching correct parent
                while len(stack) > depth:
                    stack.pop()
                stack[-1].right = node
            
            stack.append(node)  # Push new node to stack

        return stack[0]  # Root node
    
    def recoverFromPreorder(self, traversal: str) -> Optional[TreeNode]:
        idx = 0

        def back_track(depth):
            nonlocal idx
            """Recursive function to construct tree at a given depth."""
            num_dashes = 0
            while idx < len(traversal) and traversal[idx] == '-':
                num_dashes += 1
                idx += 1
            
            if num_dashes != depth:  # If depth mismatch, backtrack
                idx -= num_dashes  # Reset index for parent call
                return None
            
            # Extract node value
            value = 0
            while idx < len(traversal) and traversal[idx].isdigit():
                value = value * 10 + int(traversal[idx])
                idx += 1
            
            node = TreeNode(value)  # Create new node
            
            # Recursively construct left and right children
            node.left = back_track(depth + 1)
            node.right = back_track(depth + 1)
            
            return node

        
        return back_track(0)