class OnesCounter2D:
    def __init__(self, matrix):
        if not matrix or not matrix[0]:
            raise ValueError("Matrix must be non-empty")
        
        self.rows = len(matrix)
        self.cols = len(matrix[0])
        
        # Initialize prefix sum matrix
        self.prefix = [[0] * (self.cols + 1) for _ in range(self.rows + 1)]
        
        # Build prefix sum
        for i in range(self.rows):
            for j in range(self.cols):
                self.prefix[i + 1][j + 1] = (
                    matrix[i][j]
                    + self.prefix[i][j + 1]
                    + self.prefix[i + 1][j]
                    - self.prefix[i][j]
                )

    def query(self, x1, y1, x2, y2):
        # convert to 1-based indexing for prefix matrix
        # the other two points: top right: (x1, y2), bottom left: (x2, y1)
        x1 += 1
        y1 += 1
        x2 += 1
        y2 += 1
        return (
            self.prefix[x2][y2]
            - self.prefix[x1 - 1][y2]
            - self.prefix[x2][y1 - 1]
            + self.prefix[x1 - 1][y1 - 1]
        )


matrix = [
    [0, 1, 1, 1],
    [1, 1, 0, 1],
    [0, 0, 1, 1],
    [1, 1, 0, 1]
]

counter = OnesCounter2D(matrix)
print(counter.query(0, 0, 1, 1))  # Output: 3
print(counter.query(1, 1, 2, 2))  # Output: 2