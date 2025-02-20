class Solution:
    """
    You are given two strings s1 and s2 of equal length consisting of letters "x" and "y" only. Your task is to make these two strings equal to each other. You can swap any two characters that belong to different strings, which means: swap s1[i] and s2[j].

    Return the minimum number of swaps required to make s1 and s2 equal, or return -1 if it is impossible to do so.

    Example 1:

    Input: s1 = "xx", s2 = "yy"
    Output: 1
    Explanation: Swap s1[0] and s2[1], s1 = "yx", s2 = "yx".
    Example 2:

    Input: s1 = "xy", s2 = "yx"
    Output: 2
    Explanation: Swap s1[0] and s2[0], s1 = "yy", s2 = "xx".
    Swap s1[0] and s2[1], s1 = "xy", s2 = "xy".
    Note that you cannot swap s1[0] and s1[1] to make s1 equal to "yx", cause we can only swap chars in different strings.
    Example 3:

    Input: s1 = "xx", s2 = "xy"
    Output: -1
    """
    def minimumSwap(self, s1: str, s2: str) -> int:
        # Count mismatched pairs
        xy_count = 0  # count of (x in s1, y in s2) pairs
        yx_count = 0  # count of (y in s1, x in s2) pairs
        
        for i in range(len(s1)):
            if s1[i] != s2[i]:  # If characters don't match
                if s1[i] == 'x':
                    xy_count += 1
                else:
                    yx_count += 1
        
        # If total mismatches is odd, we can't make strings equal
        if (xy_count + yx_count) % 2 != 0:
            return -1
        
        # Calculate minimum swaps:
        # - For every 2 pairs of xy, we need 1 swap
        # - For every 2 pairs of yx, we need 1 swap
        # - For 1 xy and 1 yx, we need 2 swaps
        
        # Integer division by 2
        swaps = xy_count // 2 + yx_count // 2
        
        # If there are remaining pairs (must be 1 xy and 1 yx)
        if xy_count % 2 == 1:
            swaps += 2
        
        return swaps