class Solution:
    """
    You are given an array of integers stones where stones[i] is the weight of the ith stone.

    We are playing a game with the stones. On each turn, we choose any two stones and smash them together. Suppose the stones have weights x and y with x <= y. The result of this smash is:

    If x == y, both stones are destroyed, and
    If x != y, the stone of weight x is destroyed, and the stone of weight y has new weight y - x.
    At the end of the game, there is at most one stone left.

    Return the smallest possible weight of the left stone. If there are no stones left, return 0.

    Example 1:

    Input: stones = [2,7,4,1,8,1]
    Output: 1
    Explanation:
    We can combine 2 and 4 to get 2, so the array converts to [2,7,1,8,1] then,
    we can combine 7 and 8 to get 1, so the array converts to [2,1,1,1] then,
    we can combine 2 and 1 to get 1, so the array converts to [1,1,1] then,
    we can combine 1 and 1 to get 0, so the array converts to [1], then that's the optimal value.
    Example 2:

    Input: stones = [31,26,33,21,40]
    Output: 5
    """
    def lastStoneWeightII1(self, stones: List[int]) -> int:
        """
        time limit exceeded
        """
        if not stones:
            return 0
        if len(stones) == 1:
            return stones[0]

        def helper(path: List[int]):
            if not path:
                return float('inf')
            if len(path) == 1:
                return path[0]
            res = float('inf')
            for i in range(len(path)):
                for j in range(i + 1, len(path)):
                    next = path[:i] + path[i + 1:j] + path[j + 1:]
                    if path[i] == path[j]:
                        res = min(res, helper(next))
                    else:
                        res = min(res, helper(next + [abs(path[i] - path[j])]))
            return res
        return helper(stones)
    
    def lastStoneWeightII(self, stones: List[int]) -> int:
        """
        Aim to get as close to this as possible
        """
        sums = sum(stones)
        n = len(stones)
        @cache
        def helper(idx: int, cur_sum: int) -> int:
            """
            try to split the stones into two subsets, the difference between the two subsets is as small as possible
            """
            if idx == n:
                # Difference between two subsets
                return abs((sums - cur_sum) - cur_sum)
            # Try including or excluding the current stone
            return min(helper(idx + 1, cur_sum + stones[idx]), helper(idx + 1, cur_sum))
        
        return helper(0, 0)