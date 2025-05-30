from typing import List


class Solution:
    """
        Given two integer arrays pushed and popped each with distinct values, return true if this could have been the result of a sequence of push and pop operations on an initially empty stack, or false otherwise.

        Example 1:

        Input: pushed = [1,2,3,4,5], popped = [4,5,3,2,1]
        Output: true
        Explanation: We might do the following sequence:
        push(1), push(2), push(3), push(4),
        pop() -> 4,
        push(5),
        pop() -> 5, pop() -> 3, pop() -> 2, pop() -> 1
        Example 2:

        Input: pushed = [1,2,3,4,5], popped = [4,3,5,1,2]
        Output: false
        Explanation: 1 cannot be popped before 2.
    """
    def validateStackSequences1(self, pushed: List[int], popped: List[int]) -> bool:
        stack = []
        j = 0
        for x in pushed:
            stack.append(x)
            while stack and j < len(popped) and stack[-1] == popped[j]:
                stack.pop()
                j += 1
        return j == len(popped)
    
    def validateStackSequences2(self, pushed: List[int], popped: List[int]) -> bool:
        stack, idx = [], 0
        n = len(popped)
        for num in pushed:
            stack.append(num)
            while stack and idx < n and stack[-1] == popped[idx]:
                stack.pop()
                idx += 1
        return idx == n