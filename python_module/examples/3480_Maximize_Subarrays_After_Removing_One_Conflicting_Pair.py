class Solution:
    """
    You are given an integer n which represents an array nums containing the numbers from 1 to n in order. Additionally, you are given a 2D array conflictingPairs, where conflictingPairs[i] = [a, b] indicates that a and b form a conflicting pair.

    Remove exactly one element from conflictingPairs. Afterward, count the number of non-empty subarrays of nums which do not contain both a and b for any remaining conflicting pair [a, b].

    Return the maximum number of subarrays possible after removing exactly one conflicting pair.

    Example 1:

    Input: n = 4, conflictingPairs = [[2,3],[1,4]]

    Output: 9

    Explanation:

    Remove [2, 3] from conflictingPairs. Now, conflictingPairs = [[1, 4]].
    There are 9 subarrays in nums where [1, 4] do not appear together. They are [1], [2], [3], [4], [1, 2], [2, 3], [3, 4], [1, 2, 3] and [2, 3, 4].
    The maximum number of subarrays we can achieve after removing one element from conflictingPairs is 9.
    Example 2:

    Input: n = 5, conflictingPairs = [[1,2],[2,5],[3,5]]

    Output: 12

    Explanation:

    Remove [1, 2] from conflictingPairs. Now, conflictingPairs = [[2, 5], [3, 5]].
    There are 12 subarrays in nums where [2, 5] and [3, 5] do not appear together.
    The maximum number of subarrays we can achieve after removing one element from conflictingPairs is 12.
    """
    def maxSubarrays(self, n: int, conflictingPairs: List[List[int]]) -> int:
        bMin1 = [2**31 - 1] * (n + 1)
        bMin2 = [2**31 - 1] * (n + 1)
        for pair in conflictingPairs:
            a = min(pair[0], pair[1])
            b = max(pair[0], pair[1])
            if bMin1[a] > b:
                bMin2[a] = bMin1[a]
                bMin1[a] = b
            elif bMin2[a] > b:
                bMin2[a] = b
        res = 0
        ib1 = n
        b2 = 0x3FFFFFFF
        delCount = [0] * (n + 1)
        for i in range(n, 0, -1):
            if bMin1[ib1] > bMin1[i]:
                b2 = min(b2, bMin1[ib1])
                ib1 = i
            else:
                b2 = min(b2, bMin1[i])
            res += min(bMin1[ib1], n + 1) - i
            delCount[ib1] += min(min(b2, bMin2[ib1]), n + 1) - min(
                bMin1[ib1], n + 1
            )
        return res + max(delCount)