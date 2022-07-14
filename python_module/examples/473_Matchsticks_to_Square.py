from collections import Counter
from functools import lru_cache
from typing import List


class Solution:
    """
        You are given an integer array matchsticks where matchsticks[i] is the length of the ith matchstick. You want to use all the matchsticks to make one square. You should not break any stick, but you can link them up, and each matchstick must be used exactly one time.

        Return true if you can make this square and false otherwise.

        Example 1:

        Input: matchsticks = [1,1,2,2,2]
        Output: true
        Explanation: You can form a square with length 2, one side of the square came two sticks with length 1.
        Example 2:

        Input: matchsticks = [3,3,3,3,4]
        Output: false
        Explanation: You cannot find a way to form a square with all the matchsticks.

        Constraints:

        1 <= matchsticks.length <= 15
        1 <= matchsticks[i] <= 108
    """
    def makesquare1(self, matchsticks: List[int]) -> bool:
        if not matchsticks or len(matchsticks) < 4:
            return False
        sums = sum(matchsticks)
        if sums % 4 != 0:
            return False

        def discoverSubsequences(sourceArray, targetArray, idx, accumateSum, target):
            if accumateSum == target:
                return targetArray
            elif accumateSum > target or idx == len(sourceArray):
                return []

            withElement = discoverSubsequences(sourceArray, targetArray + [sourceArray[idx]], idx + 1, accumateSum + sourceArray[idx], target)
            if withElement:
                return withElement
            return discoverSubsequences(sourceArray, targetArray, idx + 1, accumateSum, target)

        oldArray = matchsticks.copy()
        newArray = []
        for i in range(4):
            oldArray = list((Counter(oldArray) - Counter(newArray)).elements())
            newArray = discoverSubsequences(oldArray, [], 0, 0, sums // 4)
            if not newArray:
                return False
        return oldArray == newArray

    def makesquare2(self, matchsticks: List[int]) -> bool:
        if not matchsticks or len(matchsticks) < 4:
            return False
        s = sum(matchsticks)
        if s % 4 != 0:
            return False
        possibleSide = s // 4

        sums = [0 for _ in range(4)]
        def dfs(idx:int) -> bool:
            if idx == len(matchsticks):
                return sums[0] == sums[1] == sums[2] == possibleSide
            for i in range(4):
                sums[i] += matchsticks[idx]
                if dfs(idx + 1):
                    return True
                sums[i] -= matchsticks[idx]

                if sums[i] == 0:
                    break
            return False

        return dfs(0)

    def makesquare(self, matchsticks: List[int]) -> bool:
        # There should be at least 4 matchsticks.
        if len(matchsticks) < 4:
            return False

        # Sum of matchstick lengths should be divisble by four.
        side_length, remainder = divmod(sum(matchsticks), 4)
        if remainder != 0:
            return False

        # There shouldn't be any single matchstick with length greater than side_length.
        if max(matchsticks) > side_length:
            return False

        # Check if partitioning is possible.
        return self.can_partition(matchsticks, 4, side_length)

    def can_partition(self, nums, k, target):
        buckets = [0] * k
        nums.sort(reverse=True)  # make it running faster

        def backtrack(idx):
            # If all elements have been used, check if all are equal.
            if idx == len(nums):
                return len(set(buckets)) == 1

            # Try placing numbers in each bucket.
            for i in range(k):
                buckets[i] += nums[idx]
                if buckets[i] <= target and backtrack(idx + 1):
                    return True
                buckets[i] -= nums[idx]

                # Pruning: Buckets are filled from left to right. If any bucket remains empty,
                # then all buckets to the right of it will also be empty.
                if buckets[i] == 0:
                    break

            return False

        return backtrack(0)

if __name__ == "__main__":
    solution = Solution()
    matchsticks = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15]
    print(solution.makesquare(matchsticks))
