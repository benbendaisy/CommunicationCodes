class Solution:
    """
    You are given a 0-indexed 2D integer array peaks where peaks[i] = [xi, yi] states that mountain i has a peak at coordinates (xi, yi). A mountain can be described as a right-angled isosceles triangle, with its base along the x-axis and a right angle at its peak. More formally, the gradients of ascending and descending the mountain are 1 and -1 respectively.

    A mountain is considered visible if its peak does not lie within another mountain (including the border of other mountains).

    Return the number of visible mountains.

    Example 1:

    Input: peaks = [[2,2],[6,3],[5,4]]
    Output: 2
    Explanation: The diagram above shows the mountains.
    - Mountain 0 is visible since its peak does not lie within another mountain or its sides.
    - Mountain 1 is not visible since its peak lies within the side of mountain 2.
    - Mountain 2 is visible since its peak does not lie within another mountain or its sides.
    There are 2 mountains that are visible.
    Example 2:

    Input: peaks = [[1,3],[1,3]]
    Output: 0
    Explanation: The diagram above shows the mountains (they completely overlap).
    Both mountains are not visible since their peaks lie within each other.
    """
    def visibleMountains1(self, peaks: List[List[int]]) -> int:
        counter = defaultdict(int)
        for x, y in peaks:
            counter[(x, y)] += 1
        peaks = sorted(counter.keys())
        if not peaks:
            return 0
        def within(x, y):
            x1, y1 = x
            x2, y2 = y
            b1 = y1 - x1
            b2 = y1 + x1
            return y2 <= x2 + b1 and y2 <= -x2 + b2
        n = len(peaks)
        stack = [tuple(peaks[0])]
        for x, y in peaks[1:]:
            while stack and within((x, y), stack[-1]):
                stack.pop()
            if not stack or not within(stack[-1], (x, y)):
                stack.append((x, y))
        return len([p for p in stack if counter[p] == 1])

    def visibleMountains(self, peaks: List[List[int]]) -> int:
        if not peaks:
            return 0
        freq = defaultdict(int)
        for x, y in peaks:
            freq[(x, y)] += 1
        
        peaks = sorted(freq.keys())
        def within(x, y):
            x1, y1 = x
            x2, y2 = y
            b1 = y1 - x1
            b2 = y1 + x1
            return y2 <= x2 + b1 and y2 <= -x2 + b2
        
        stack = [tuple(peaks[0])]
        for x, y in peaks[1:]:
            while stack and within((x, y), stack[-1]):
                stack.pop()
            if not stack or not within(stack[-1], (x, y)):
                stack.append((x, y))
            
        return len([p for p in stack if freq[p] == 1])