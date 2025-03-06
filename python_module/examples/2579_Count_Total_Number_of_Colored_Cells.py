class Solution:
    """
    There exists an infinitely large two-dimensional grid of uncolored unit cells. You are given a positive integer n, indicating that you must do the following routine for n minutes:

    At the first minute, color any arbitrary unit cell blue.
    Every minute thereafter, color blue every uncolored cell that touches a blue cell.
    Below is a pictorial representation of the state of the grid after minutes 1, 2, and 3.

    Return the number of colored cells at the end of n minutes.

    Example 1:

    Input: n = 1
    Output: 1
    Explanation: After 1 minute, there is only 1 blue cell, so we return 1.
    Example 2:

    Input: n = 2
    Output: 5
    Explanation: After 2 minutes, there are 4 colored cells on the boundary and 1 in the center, so we return 5. 
    """
    def coloredCells1(self, n: int) -> int:
        def helper(m: int) -> int:
            if m == 1:
                return 1
            return helper(m - 1) + 4 * (m - 1)
        return helper(n)
    
    def coloredCells(n):
        # If n is 1, we only color the initial cell
        if n == 1:
            return 1
        
        # Initialize the number of colored cells
        # The first minute always colors 1 cell
        colored_cells = 1
        
        # Track the additional cells colored in each subsequent minute
        additional_cells = 1
        
        # Simulate coloring for each minute after the first
        for minute in range(2, n + 1):
            # Calculate additional cells colored this minute
            # The pattern increases by 4 * (minute - 1)
            additional_cells += 4 * (minute - 1)
            colored_cells += additional_cells
        
        return colored_cells