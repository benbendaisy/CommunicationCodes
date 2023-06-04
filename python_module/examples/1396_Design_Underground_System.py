import collections
from collections import defaultdict
from statistics import mean


class UndergroundSystem1:

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

class UndergroundSystem:

    def __init__(self):
        self.member_cache = {}
        self.station_cache = defaultdict(list)

    def checkIn(self, id: int, stationName: str, t: int) -> None:
        if id not in self.member_cache:
            self.member_cache[id] = (stationName, t)

    def checkOut(self, id: int, stationName: str, t: int) -> None:
        if id in self.member_cache:
            self.station_cache[(self.member_cache[id][0], stationName)].append(t - self.member_cache[id][1])
            del self.member_cache[id]

    def getAverageTime(self, startStation: str, endStation: str) -> float:
        if (startStation, endStation) not in self.station_cache:
            return 0.0
        travel_times = self.station_cache[(startStation, endStation)]
        return sum(travel_times) * 1.0 / len(travel_times)

if __name__ == "__main__":
    obj = UndergroundSystem()
    obj.checkIn(45,"Leyton",3)
    obj.checkOut(45,"Waterloo",15)
    param_3 = obj.getAverageTime("Leyton","Waterloo")
    print(param_3)