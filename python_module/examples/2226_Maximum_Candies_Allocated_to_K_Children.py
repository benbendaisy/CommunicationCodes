class Solution:
    """
    You are given a 0-indexed integer array candies. Each element in the array denotes a pile of candies of size candies[i]. You can divide each pile into any number of sub piles, but you cannot merge two piles together.

    You are also given an integer k. You should allocate piles of candies to k children such that each child gets the same number of candies. Each child can be allocated candies from only one pile of candies and some piles of candies may go unused.

    Return the maximum number of candies each child can get.

    Example 1:

    Input: candies = [5,8,6], k = 3
    Output: 5
    Explanation: We can divide candies[1] into 2 piles of size 5 and 3, and candies[2] into 2 piles of size 5 and 1. We now have five piles of candies of sizes 5, 5, 3, 5, and 1. We can allocate the 3 piles of size 5 to 3 children. It can be proven that each child cannot receive more than 5 candies.
    Example 2:

    Input: candies = [2,5], k = 11
    Output: 0
    Explanation: There are 11 children but only 7 candies in total, so it is impossible to ensure each child receives at least one candy. Thus, each child gets no candy and the answer is 0.
    """
    def maximumCandies1(self, candies: List[int], k: int) -> int:
        if not candies or sum(candies) < k:
            return 0

        n = len(candies)

        @cache
        def helper(idx: int, candie: int, remaining: int) -> bool:
            if remaining <= 0:
                return True
            if idx == n:
                return False

            # Compute how many kids can take `candie` size from current pile
            max_kids = candies[idx] // candie
            if helper(idx + 1, candie, remaining - max_kids):
                return True
            return False
        # Binary search for max candies per kid
        left, right = 1, max(candies)
        best = 0
        while left <= right:
            mid = (left + right) // 2
            if helper(0, mid, k):
                best = mid
                left = mid + 1  # Try for more candies per kid
            else:
                right = mid - 1  # Reduce the number of candies per kid

        return best

    def maximumCandies(self, candies: List[int], k: int) -> int:
        if not candies or sum(candies) < k:
            return 0

        n = len(candies)

        # @cache
        def helper(idx: int, candie: int, remaining: int) -> bool:
            if remaining <= 0:
                return True
            if idx == n:
                return False

            max_kids = candies[idx] // candie
            if helper(idx + 1, candie, remaining - max_kids):
                return True
            return False
        ave = sum(candies) // k
        left, right = 1, ave
        max_candies = 0
        while left <= right:
            mid = (left + right) // 2
            if helper(0, mid, k):
                max_candies = mid
                left = mid + 1
            else:
                right = mid - 1
        return max_candies