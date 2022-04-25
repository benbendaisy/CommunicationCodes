import collections
from collections import defaultdict
from statistics import mean


class UndergroundSystem:

    def __init__(self):
        self.averageCache = defaultdict(list)
        self.checkInMap = {}
        self.journey_data = collections.defaultdict(lambda : [0, 0])

    def checkIn(self, id: int, stationName: str, t: int) -> None:
        self.checkInMap[id] = (stationName, t)

    def checkOut(self, id: int, stationName: str, t: int) -> None:
        startStation, t1 = self.checkInMap.pop(id)
        self.averageCache[startStation + ":" + stationName].append(t - t1)

    def getAverageTime(self, startStation: str, endStation: str) -> float:
        return mean(self.averageCache[startStation + ":" + endStation])

if __name__ == "__main__":
    obj = UndergroundSystem()
    obj.checkIn(45,"Leyton",3)
    obj.checkOut(45,"Waterloo",15)
    param_3 = obj.getAverageTime("Leyton","Waterloo")
    print(param_3)