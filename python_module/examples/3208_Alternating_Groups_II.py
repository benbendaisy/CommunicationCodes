class Solution:
    """
    here is a circle of red and blue tiles. You are given an array of integers colors and an integer k. The color of tile i is represented by colors[i]:

    colors[i] == 0 means that tile i is red.
    colors[i] == 1 means that tile i is blue.
    An alternating group is every k contiguous tiles in the circle with alternating colors (each tile in the group except the first and last one has a different color from its left and right tiles).

    Return the number of alternating groups.

    Note that since colors represents a circle, the first and the last tiles are considered to be next to each other.

    Example 1:

    Input: colors = [0,1,0,1,0], k = 3

    Output: 3

    Explanation:

    Alternating groups:

    Example 2:

    Input: colors = [0,1,0,0,1,0,1], k = 6

    Output: 2

    Explanation:

    Alternating groups:

    Example 3:

    Input: colors = [1,1,0,1], k = 4

    Output: 0

    Explanation:
    """
    def numberOfAlternatingGroups1(self, colors: List[int], k: int) -> int:
        """
        TLE
        """
        if not colors:
            return 0
        n = len(colors)
        if n < k:
            return 0  # Not enough elements to form a group
        
        @cache
        def is_alternating(start, remaining):
            if remaining == 1:
                return True  # Base case: single element is always valid
            start = start % n
            nxt = (start + 1) % n
            if colors[start] == colors[nxt]:  
                return False  # Consecutive elements should not be the same
            return is_alternating(start + 1, remaining - 1)

        count = 0
        for i in range(n):  # Ensure we do not go out of bounds
            if is_alternating(i, k):
                count += 1

        return count
    
    def numberOfAlternatingGroups2(self, colors: List[int], k: int) -> int:
        if not colors or len(colors) < k:
            return 0

        n = len(colors)
        count = 0

        # Check every possible starting position
        for i in range(n):
            is_alternating = True

            # Check if k-length subarray follows the alternating pattern
            for j in range(k - 1):  
                curr_idx = (i + j) % n
                next_idx = (i + j + 1) % n

                if colors[curr_idx] == colors[next_idx]:  # If two consecutive tiles are same, not alternating
                    is_alternating = False
                    break

            if is_alternating:
                count += 1

        return count
    
    def numberOfAlternatingGroups(self, colors: List[int], k: int) -> int:
        if not colors or len(colors) < k:
            return 0

        n = len(colors)
        w, res = 1, 0
        for i in range(1, n + k - 1):
            if colors[i % n] != colors[(i - 1) % n]:
                w += 1
            else:
                w = 1
            if w >= k:
                res += 1
        return res
