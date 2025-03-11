class Solution:
    """
    You are given a 0-indexed string blocks of length n, where blocks[i] is either 'W' or 'B', representing the color of the ith block. The characters 'W' and 'B' denote the colors white and black, respectively.

    You are also given an integer k, which is the desired number of consecutive black blocks.

    In one operation, you can recolor a white block such that it becomes a black block.

    Return the minimum number of operations needed such that there is at least one occurrence of k consecutive black blocks.

    Example 1:

    Input: blocks = "WBBWWBBWBW", k = 7
    Output: 3
    Explanation:
    One way to achieve 7 consecutive black blocks is to recolor the 0th, 3rd, and 4th blocks
    so that blocks = "BBBBBBBWBW". 
    It can be shown that there is no way to achieve 7 consecutive black blocks in less than 3 operations.
    Therefore, we return 3.
    Example 2:

    Input: blocks = "WBWBBBW", k = 2
    Output: 0
    Explanation:
    No changes need to be made, since 2 consecutive black blocks already exist.
    Therefore, we return 0.
    """
    def minimumRecolors1(self, blocks: str, k: int) -> int:
        # Count 'W's in the first window of size k
        min_recolor = blocks[:k].count('W')
        current_recolor = min_recolor
        
        # Slide the window across the string
        for i in range(k, len(blocks)):
            # Remove the effect of the leftmost character and add the rightmost one
            if blocks[i - k] == 'W':
                current_recolor -= 1
            if blocks[i] == 'W':
                current_recolor += 1
            
            # Update the minimum recolor needed
            min_recolor = min(min_recolor, current_recolor)
        
        return min_recolor
    
    def minimumRecolors(self, blocks: str, k: int) -> int:
        min_color = blocks[:k].count('W')
        running_color = min_color
        for i in range(k, len(blocks)):
            if blocks[i - k] == 'W':
                running_color -= 1
            if blocks[i] == 'W':
                running_color += 1
            min_color = min(min_color, running_color)
        return min_color