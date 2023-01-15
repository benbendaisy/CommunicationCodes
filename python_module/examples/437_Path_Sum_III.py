# Definition for a binary tree node.
from collections import defaultdict
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> int:
        def path_sums(node, current_sum):
            if not node:
                return
            nonlocal count
            # current prefix sum
            current_sum += node.val

            # here is the sum we're looking for
            if current_sum == k:
                count += 1

            # number of times the curr_sum − k has occurred already,
            # determines the number of times a path with sum k
            # has occurred up to the current node
            count += h_dict[current_sum - k]

            # add the current sum into hashmap
            # to use it during the child nodes processing
            h_dict[current_sum] += 1
            # process left subtree
            path_sums(node.left, current_sum)
            # process right subtree
            path_sums(node.right, current_sum)
            # remove the current sum from the hashmap
            # in order not to use it during
            # the parallel subtree processing
            h_dict[current_sum] -= 1
        count, k = 0, targetSum
        h_dict = defaultdict(int)
        path_sums(root, 0)
        return count

