import numpy as np
import csv


class SubwayLine(object):

    def __init__(self, text):
        with open(text) as f:
            csv_reader = csv.reader(f, delimiter=',')
            self.numStations = int(next(csv_reader)[0])
            self.numEdges = int(next(csv_reader)[0])
            self.adjDict = Stations()

            for line in csv_reader:
                self.addEdge(line[0], line[1])

            self.checkNumber()

    def addEdge(self, v, w):
        if v not in self.adjDict:
            self.adjDict[v]

        self.adjDict[v]["eastNorth"] = w

        if w not in self.adjDict:
            self.adjDict[w]

        self.adjDict[w]["westSouth"] = v

    def checkNumber(self):
        if self.numStations != len(self.adjDict.keys()):
            raise "Number of stations not equal to that in text file "

    def adjacent(self, v):
        return (self.adjDict[v]["eastNorth"], self.adjDict[v]["westSouth"])


class Stations(dict):
    def __missing__(self, key):
        value = self[key] = type(self)()
        return value


class Search(object):
    def __init__(self, G):
        self.marked = [False] * int(G.numStations)
        self.keys = list(G.adjDict.keys())

    def depthFirstSearch(self, G, s):
        self.marked[self.keys.index(s)] = True
        for stations in G.adjDict[s].items():
            if not self.marked[self.keys.index(stations[1])]:
                self.depthFirstSearch(G, stations[1])

    def count(self):
        print(f"The number of connected stations is: {sum(self.marked)}")


system = SubwayLine('lines.txt')


eastbound = Search(system)
eastbound.depthFirstSearch(system, "BATHURST")
eastbound.count()