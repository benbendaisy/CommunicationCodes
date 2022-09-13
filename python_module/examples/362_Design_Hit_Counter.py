from collections import defaultdict


class HitCounter:

    def __init__(self):
        self.hitCache = defaultdict(int)

    def hit(self, timestamp: int) -> None:
        self.hitCache[timestamp] += 1

    def getHits(self, timestamp: int) -> int:
        cnt = 0
        for time in range(timestamp - 299, timestamp + 1):
            cnt += self.hitCache[time]
        return cnt