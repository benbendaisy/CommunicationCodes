from typing import List


class Solution:
    """
    ou are installing a billboard and want it to have the largest height. The billboard will have two steel supports, one on each side. Each steel support must be an equal height.

    You are given a collection of rods that can be welded together. For example, if you have rods of lengths 1, 2, and 3, you can weld them together to make a support of length 6.

    Return the largest possible height of your billboard installation. If you cannot support the billboard, return 0.

    Example 1:

    Input: rods = [1,2,3,6]
    Output: 6
    Explanation: We have two disjoint subsets {1,2,3} and {6}, which have the same sum = 6.
    Example 2:

    Input: rods = [1,2,3,4,5,6]
    Output: 10
    Explanation: We have two disjoint subsets {2,3,5} and {4,6}, which have the same sum = 10.
    Example 3:

    Input: rods = [1,2]
    Output: 0
    Explanation: The billboard cannot be supported, so we return 0.
    """
    def tallestBillboard1(self, rods: List[int]) -> int:
        sums = sum(rods)
        dp = [-1] * (sums + 1)
        dp[0] = 0
        for rod in rods:
            deep_copy = dp[:]
            for i in range(sums - rod + 1):
                if deep_copy[i] < 0:
                    continue
                dp[i + rod] = max(dp[i + rod], deep_copy[i])
                dp[abs(i - rod)] = max(dp[abs(i - rod)], deep_copy[i] + min(i, rod))
        return dp[0]
    
    def tallestBillboard2(self, rods: List[int]) -> int:
        
        # Left pile stands for steel support on left hand side
        # Right pile stands for steel support on right hand side

        ## DP table
        # key: differnece of left pile to right pile. 
        # Define diff = sum(left pile) - sum(right pile)

        # value: max height of left pile = max{ each possible sum(left pile) }
        dp = defaultdict(int)

        # Initialization:
        # Left pile = Right pile = 0
        # Build steel base from height = 0
        dp[0] = 0

        # Use one steel for each round
        for rod in rods:

            # Update building status
            # Put current steel either to left pile or right pile, or just discard (skip, not to use)
            for diff, height_of_left_pile in list(dp.items()):
                
                # Put current steel on left pile
                dp[ diff + rod ] = max(dp[ diff + rod ], height_of_left_pile + rod)

                # Put current steel on right pile
                dp[ diff - rod ] = max( dp[ diff - rod ], height_of_left_pile)

                # Discard current steel, nothing happen to current building status
                # we do nothing here in this case.

        # Final goal:
        # We want maximal reachable height of billboard with left pile equal to right pile
        # => We want maximal reachable height of billboard with difference = 0, with two equal steel support on both sides.
        return dp[0]
    
    def tallestBillboard(self, rods: List[int]) -> int:
        def building(idx):
            if idx < 0:
                init = defaultdict(int)
                init[0] = 0
                return init
            prev = building(idx - 1)
            memo = prev.copy()
            # Update building status
            # Put current steel either to left pile or right pile, or just discard (skip, not to use)
            for diff, height_of_left_pile in prev.items():
                # Put current steel on left pile
                memo[diff + rods[idx]] = max(memo[diff + rods[idx]], height_of_left_pile + rods[idx])
                # Put current steel on right pile
                memo[diff - rods[idx]] = max(memo[diff - rods[idx] ], height_of_left_pile)
                # Discard current steel, nothing happen to current building status
                # we do nothing here in this case.
            return memo
        return building(len(rods)-1)[0]