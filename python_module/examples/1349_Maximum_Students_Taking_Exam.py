class Solution:
    """
    Given a m * n matrix seats  that represent seats distributions in a classroom. If a seat is broken, it is denoted by '#' character otherwise it is denoted by a '.' character.

    Students can see the answers of those sitting next to the left, right, upper left and upper right, but he cannot see the answers of the student sitting directly in front or behind him. Return the maximum number of students that can take the exam together without any cheating being possible.

    Students must be placed in seats in good condition.

    Example 1:

    Input: seats = [["#",".","#","#",".","#"],
                    [".","#","#","#","#","."],
                    ["#",".","#","#",".","#"]]
    Output: 4
    Explanation: Teacher can place 4 students in available seats so they don't cheat on the exam. 
    Example 2:

    Input: seats = [[".","#"],
                    ["#","#"],
                    ["#","."],
                    ["#","#"],
                    [".","#"]]
    Output: 3
    Explanation: Place all students in available seats. 

    Example 3:

    Input: seats = [["#",".",".",".","#"],
                    [".","#",".","#","."],
                    [".",".","#",".","."],
                    [".","#",".","#","."],
                    ["#",".",".",".","#"]]
    Output: 10
    Explanation: Place students in available seats in column 1, 3 and 5.
    """
    def maxStudents(self, seats: List[List[str]]) -> int:
        m, n = len(seats), len(seats[0])
        valid_rows = []

        for row in seats:
            mask = 0
            for j in range(n):
                if row[j] == '.':
                    mask |= (1 << j)
            valid_rows.append(mask)

        memo = {}

        def count_bits(x):
            return bin(x).count('1')
        
        def valid(mask):
            return (mask & (mask >> 1)) == 0
        
        def dfs(idx, prev_mask):
            if idx == m:
                return 0
            if (idx, prev_mask) in memo:
                return memo[(idx, prev_mask)]
            
            res = 0
            row_mask = valid_rows[idx]

            mask = row_mask
            while mask >= 0:
                if (mask & row_mask) == mask and valid(mask):
                    if (mask & prev_mask) == 0 and ((mask >> 1) & prev_mask) == 0:
                        res = max(res, count_bits(mask) + dfs(idx + 1, mask))
                
                if mask == 0:
                    break
                mask = (mask - 1) & row_mask

            memo[(idx, prev_mask)] = res
            return res
        
        return dfs(0, 0)