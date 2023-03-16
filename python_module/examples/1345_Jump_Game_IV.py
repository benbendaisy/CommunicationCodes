from collections import defaultdict, deque
from typing import List


class Solution:
    """
        Given an array of integers arr, you are initially positioned at the first index of the array.

        In one step you can jump from index i to index:

        i + 1 where: i + 1 < arr.length.
        i - 1 where: i - 1 >= 0.
        j where: arr[i] == arr[j] and i != j.
        Return the minimum number of steps to reach the last index of the array.

        Notice that you can not jump outside of the array at any time.

        Example 1:

        Input: arr = [100,-23,-23,404,100,23,23,23,3,404]
        Output: 3
        Explanation: You need three jumps from index 0 --> 4 --> 3 --> 9. Note that index 9 is the last index of the array.
        Example 2:

        Input: arr = [7]
        Output: 0
        Explanation: Start index is the last index. You do not need to jump.
        Example 3:

        Input: arr = [7,6,9,6,9,6,9,7]
        Output: 1
        Explanation: You can jump directly from index 0 to index 7 which is last index of the array.
    """
    def minJumps(self, arr: List[int]) -> int:
        n = len(arr)
        if n == 1:
            return 0

        # Create a dictionary to store the indices of each value in the array
        indices = defaultdict(list)
        for i, num in enumerate(arr):
            indices[num].append(i)

        # Initialize variables for the BFS algorithm
        visited = set()
        que = deque([(0, 0)])

        while que:
            index, steps = que.popleft()
            # Check if we have reached the end of the array
            if index == n - 1:
                return steps

            # Add neighbors to the queue
            for neighbor in indices[arr[index]]:
                if neighbor not in visited:
                    visited.add(neighbor)
                    que.append((neighbor, steps + 1))
            # Clear the list of indices for this value, since we have already visited them
            indices[arr[index]] = []
            # Add adjacent indices to the queue
            if index - 1 not in visited and index - 1 >= 0:
                visited.add(index - 1)
                que.append((index - 1, steps + 1))
            if index + 1 not in visited and index + 1 < n:
                visited.add(index + 1)
                que.append((index + 1, steps + 1))
