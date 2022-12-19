import math
from typing import List


class Solution:
    """
        Given an array of integers arr, find the sum of min(b), where b ranges over every (contiguous) subarray of arr. Since the answer may be large, return the answer modulo 109 + 7.

        Example 1:

        Input: arr = [3,1,2,4]
        Output: 17
        Explanation:
        Subarrays are [3], [1], [2], [4], [3,1], [1,2], [2,4], [3,1,2], [1,2,4], [3,1,2,4].
        Minimums are 3, 1, 2, 4, 1, 1, 2, 1, 1, 1.
        Sum is 17.
        Example 2:

        Input: arr = [11,81,94,43,3]
        Output: 444
    """
    def sumSubarrayMins1(self, arr: List[int]) -> int:
        mod = 10 ** 9 + 7
        n = len(arr)
        sub_arrays = []
        for i in range(n):
            for j in range(i + 1, n + 1):
                sub_arrays.append(arr[i:j])
        return sum([min(x) for x in sub_arrays]) % mod

    def sumSubarrayMins2(self, arr: List[int]) -> int:
        mod = 10 ** 9 + 7
        n = len(arr)
        sum_of_mins = 0
        stack = []
        for i in range(n + 1):
            # when i reaches the array length, it is an indication that
            # all the elements have been processed, and the remaining
            # elements in the stack should now be popped out.
            while stack and (i == n or arr[stack[-1]] >= arr[i]):
                # Notice the sign ">=", This ensures that no contribution
                # is counted twice. right_boundary takes equal or smaller
                # elements into account while left_boundary takes only the
                # strictly smaller elements into account
                curr_min = stack.pop()
                left_boundary = -1 if not stack else stack[-1]
                right_boundary = i

                # count of subarrays where mid is the minimum element
                cnt = (curr_min - left_boundary) * (right_boundary - curr_min)
                sum_of_mins += cnt * arr[curr_min]
            stack.append(i)
        return sum_of_mins % mod

    def sumSubarrayMins(self, arr: List[int]) -> int:
        mod = 10 ** 9 + 7
        # monotonic increasing stack
        stack = []
        # make a dp array of the same size as the input array
        dp = [0] * len(arr)

        # populate monotonically increasing stack
        for i in range(len(arr)):
            # before pushing an element, make sure all
            # larger and equal elements in the stack are
            # removed
            while stack and arr[stack[-1]] >= arr[i]:
                stack.pop()

            # calculate the sum of minimums of all subarrays
            # ending at index i
            if stack:
                prev_small = stack[-1]
                dp[i] = dp[prev_small] + (i - prev_small) * arr[i]
            else:
                dp[i] = (i + 1) * arr[i]
            stack.append(i)
        # add all the elements of dp to get the answer
        return sum(dp) % mod
