class Solution:
    """
        The string "PAYPALISHIRING" is written in a zigzag pattern on a given number of rows like this: (you may want to display this pattern in a fixed font for better legibility)

        P   A   H   N
        A P L S I I G
        Y   I   R
        And then read line by line: "PAHNAPLSIIGYIR"

        Write the code that will take a string and make this conversion given a number of rows:

        string convert(string s, int numRows);

        Example 1:

        Input: s = "PAYPALISHIRING", numRows = 3
        Output: "PAHNAPLSIIGYIR"
        Example 2:

        Input: s = "PAYPALISHIRING", numRows = 4
        Output: "PINALSIGYAHRPI"
        Explanation:
        P     I    N
        A   L S  I G
        Y A   H R
        P     I
        Example 3:

        Input: s = "A", numRows = 1
        Output: "A"
    """
    def convert1(self, s: str, numRows: int) -> str:
        if numRows == 1:
            return s
        # Create a list of empty strings to store the zigzag pattern
        zigzag = ["" for _ in range(numRows)]
        # Initialize the current row index to 0
        row = 0
        # Initialize the step direction to 1 (to move down)
        step = 1
        # Iterate over the characters of the input string
        for ch in s:
            # Append the current character to the current row
            zigzag[row] += ch
            # If the current row is the last row, change the step direction to -1 (to move up)
            if row == numRows - 1:
                step = -1
            # If the current row is the first row, change the step direction to 1 (to move down)
            elif row == 0:
                step = 1
            # Move to the next row
            row += step
        return "".join(zigzag)
    
    def convert(self, s: str, numRows: int) -> str:
        if numRows == 1 or numRows >= len(s):
            return s
        
        rows = [''] * numRows
        index, step = 0, 1
        
        for char in s:
            rows[index] += char
            
            if index == 0:
                step = 1
            elif index == numRows - 1:
                step = -1
            
            index += step
        
        return ''.join(rows)

