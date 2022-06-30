import heapq
from typing import List


class Solution:
    """
        You are given an array target of n integers. From a starting array arr consisting of n 1's, you may perform the following procedure :

        let x be the sum of all elements currently in your array.
        choose index i, such that 0 <= i < n and set the value of arr at index i to x.
        You may repeat this procedure as many times as needed.
        Return true if it is possible to construct the target array from arr, otherwise, return false.

        Example 1:

        Input: target = [9,3,5]
        Output: true
        Explanation: Start with arr = [1, 1, 1]
        [1, 1, 1], sum = 3 choose index 1
        [1, 3, 1], sum = 5 choose index 2
        [1, 3, 5], sum = 9 choose index 0
        [9, 3, 5] Done
        Example 2:

        Input: target = [1,1,1,2]
        Output: false
        Explanation: Impossible to create target array from [1,1,1,1].
        Example 3:

        Input: target = [8,5]
        Output: true
    """
    def isPossible1(self, target: List[int]) -> bool:
        if len(target) == 1:
            return target == [1]

        totalSum = sum(target)
        target = [-num for num in target]
        heapq.heapify(target)
        while -target[0] > 1:
            largest = -target[0]
            x = largest - (totalSum - largest)
            if x < 1:
                return False
            heapq.heapreplace(target, -x)
            totalSum = totalSum - largest + x

        return True

    def isPossible(self, target: List[int]) -> bool:
        if len(target) == 1:
            return target == [1]

        totalSum = sum(target)
        target = [-num for num in target]
        heapq.heapify(target)
        while -target[0] > 1:
            largest = -target[0]
            rest = totalSum - largest
            if rest == 1:
                return True
            x = largest % rest
            if x == 0 or x == largest:
                return False
            heapq.heapreplace(target, -x)
            totalSum = totalSum - largest + x

        return True