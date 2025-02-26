class Solution:
    """
    here is a pizza with 3n slices of varying size, you and your friends will take slices of pizza as follows:

    You will pick any pizza slice.
    Your friend Alice will pick the next slice in the anti-clockwise direction of your pick.
    Your friend Bob will pick the next slice in the clockwise direction of your pick.
    Repeat until there are no more slices of pizzas.
    Given an integer array slices that represent the sizes of the pizza slices in a clockwise direction, return the maximum possible sum of slice sizes that you can pick.

    Example 1:

    Input: slices = [1,2,3,4,5,6]
    Output: 10
    Explanation: Pick pizza slice of size 4, Alice and Bob will pick slices with size 3 and 5 respectively. Then Pick slices with size 6, finally Alice and Bob will pick slice of size 2 and 1 respectively. Total = 4 + 6.
    Example 2:

    Input: slices = [8,9,8,6,1,1]
    Output: 16
    Explanation: Pick pizza slice of size 8 in each turn. If you pick slice with size 9 your partners will pick slices of size 8.
    """
    def maxSizeSlices(self, slices: List[int]) -> int:
        """
        Calculate the maximum sum of slice sizes you can pick when:
        - You pick any slice
        - Alice picks the next slice counter-clockwise (to the left)
        - Bob picks the next slice clockwise (to the right)
        - Repeat until no slices remain
        
        Args:
            slices: List of integers representing pizza slice sizes in clockwise order
            
        Returns:
            Maximum possible sum of slice sizes you can pick
        """
        if not slices:
            return 0
        n = len(slices)
        @cache
        def helper(start: int, end: int, remaining: int) -> int:
            if remaining == 0 or start > end:
                return 0

            # Option 1: Pick the slice at 'start' and skip the next two slices
            take = slices[start] + helper(start + 2, end, remaining - 1)
            # # Option 2: Skip the slice at 'start' and consider the next slice
            skip = helper(start + 1, end, remaining)
            # Return the maximum of the two options
            return max(take, skip)
        # Since you can pick at most n/3 slices, we need to run the recursion twice:
        # Once excluding the first slice and once excluding the last slice to handle the circular nature.
        # This ensures that we don't pick both the first and last slices, which would violate the rules.
        remaining = n // 3
        return max(helper(0, n - 2, remaining), helper(1, n - 1, remaining))