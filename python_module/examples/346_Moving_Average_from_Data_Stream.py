class MovingAverage1:
    """
        Given a stream of integers and a window size, calculate the moving average of all integers in the sliding window.

        Implement the MovingAverage class:

        MovingAverage(int size) Initializes the object with the size of the window size.
        double next(int val) Returns the moving average of the last size values of the stream.

        Example 1:

        Input
        ["MovingAverage", "next", "next", "next", "next"]
        [[3], [1], [10], [3], [5]]
        Output
        [null, 1.0, 5.5, 4.66667, 6.0]

        Explanation
        MovingAverage movingAverage = new MovingAverage(3);
        movingAverage.next(1); // return 1.0 = 1 / 1
        movingAverage.next(10); // return 5.5 = (1 + 10) / 2
        movingAverage.next(3); // return 4.66667 = (1 + 10 + 3) / 3
        movingAverage.next(5); // return 6.0 = (10 + 3 + 5) / 3

        Constraints:

        1 <= size <= 1000
        -105 <= val <= 105
        At most 104 calls will be made to next.
    """
    def __init__(self, size: int):
        self.size = size
        self.arr = []
        self.sums = 0


    def next(self, val: int) -> float:
        if len(self.arr) < self.size:
            self.arr.append(val)
            self.sums += val
            return self.sums / len(self.arr)

        delta = val - self.arr[0]
        self.arr.__delitem__(0)
        self.arr.append(val)
        self.sums += delta
        return self.sums / len(self.arr)

class MovingAverage:

    def __init__(self, size: int):
        self.que = []
        self.size = size
        self.sum = 0

    def next(self, val: int) -> float:
        if len(self.que) >= self.size:
            self.sum -= self.que.pop(0)
        self.sum += val
        self.que.append(val)
        return self.sum / len(self.que)