# refer to https://pythonwife.com/kruskal-and-prims-algorithm-in-python/ for more information
#Initializing the Graph Class
import heapq
import math
from asyncio import PriorityQueue
from collections import defaultdict


class Graph:
    def __init__(self, vertices):
        self.V = vertices
        self.graph = []
        self.nodes = []
        self.MST = []

    def addEdge(self, s, d, w):
        self.graph.append([s, d, w])

    def addNode(self, value):
        self.nodes.append(value)

    def printSolution(self,s,d,w):
        for s, d, w in self.MST:
            print("%s - %s: %s" % (s, d, w))

    def dijkstra(self, start_vertex):
        """
        v: Represents the number of vertices in the graph.
        edges: Represents the list of edges in the form of a matrix. For nodes u and v, self.edges[u][v] = weight of the edge.
        visited: A set which will contain the visited vertices.
        :param start_vertex: the started vertex
        :return:
        """
        D = {v:math.inf for v in range(self.V)}
        D[start_vertex] = 0

        pq = PriorityQueue()
        pq.put((0, start_vertex))

        while not pq.empty():
            (dist, current_vertex) = pq.get()
            self.visited.append(current_vertex)

            for neighbor in range(self.V):
                if self.edges[current_vertex][neighbor] != -1:
                    distance = self.edges[current_vertex][neighbor]
                    if neighbor not in self.visited:
                        old_cost = D[neighbor]
                        new_cost = D[current_vertex] + distance
                        if new_cost < old_cost:
                            pq.put((new_cost, neighbor))
                            D[neighbor] = new_cost
        return D

    #Function to implement Kruskal's Algorithm
    def kruskalAlgo(self):
        """
        The implementation of Kruskal’s algorithm is based on the following steps:

        1. Sort all the edges of the graph from low weight to high.
        2. Take the edge of the lowest weight and add it to the required spanning tree. If adding this edge creates a cycle in the graph, then reject this edge.
        3. Repeat this process until all the vertices are covered with the edges.
        """
        i, e = 0, 0
        ds = DisjointSet(self.nodes)
        self.graph = sorted(self.graph, key=lambda item: item[2])
        while e < self.V - 1:
            s, d, w = self.graph[i]
            i += 1
            x = ds.find(s)
            y = ds.find(d)
            if x != y:
                e += 1
                self.MST.append([s,d,w])
                ds.union(x,y)
        self.printSolution(s,d,w)

    #Function to implement Prim's Algorithm
    def primsAlgo(self):
        """
            The implementation of Prim’s algorithm is based on the following steps:

            1. Take any vertex as the source and set its weight to 0. Set the weights of all other vertices to infinity.
            2. For every adjacent vertices, if the current weight is more than that of the current edge, then we replace it with the weight of the current edge.
            3. Then, we mark the current vertex as visited.
            4. Repeat these steps for all the given vertices in ascending order of weight.
        """
        visited = [0]*self.vertexNum
        edgeNum=0
        visited[0]=True
        while edgeNum<self.vertexNum-1:
            min = math.inf
            for i in range(self.vertexNum):
                if visited[i]:
                    for j in range(self.vertexNum):
                        if ((not visited[j]) and self.edges[i][j]):
                            if min > self.edges[i][j]:
                                min = self.edges[i][j]
                                s = i
                                d = j
            self.MST.append([self.nodes[s], self.nodes[d], self.edges[s][d]])
            visited[d] = True
            edgeNum += 1
        self.printSolution()

    def create_spanning_tree(self, starting_vertex):
        """
        prim algorithm with heap
        :param starting_vertex:
        :return:
        """
        mst = defaultdict(set)
        visited = set([starting_vertex])
        edges = [
            (cost, starting_vertex, to) for to, cost in self.graph[starting_vertex].items()
        ]
        heapq.heapify(edges)

        while edges:
            cost, frm, to = heapq.heappop(edges)
            if to not in visited:
                visited.add(to)
                mst[frm].add(to)
                for to_next, cost in self.graph[to].items():
                    if to_next not in visited:
                        heapq.heappush(edges, (cost, to, to_next))

        return mst

#Implementing Disjoint Set data structure and its functions
class DisjointSet:
    def __init__(self, vertices):
        self.vertices = vertices
        self.parent = {}
        for v in vertices:
            self.parent[v] = v
        self.rank = dict.fromkeys(vertices, 0)

    def find(self, item):
        if self.parent[item] == item:
            return item

        return self.find(self.parent[item])

    def union(self, x, y):
        xroot = self.find(x)
        yroot = self.find(y)
        if self.rank[xroot] < self.rank[yroot]:
            self.parent[xroot] = yroot
        elif self.rank[xroot] > self.rank[yroot]:
            self.parent[yroot] = xroot
        else:
            self.parent[yroot] = xroot
            self.rank[xroot] += 1

g = Graph(5)
g.addNode("A")
g.addNode("B")
g.addNode("C")
g.addNode("D")
g.addNode("E")
g.addEdge("A", "B", 5)
g.addEdge("A", "C", 13)
g.addEdge("A", "E", 15)
g.addEdge("B", "A", 5)
g.addEdge("B", "C", 10)
g.addEdge("B", "D", 8)
g.addEdge("C", "A", 13)
g.addEdge("C", "B", 10)
g.addEdge("C", "E", 20)
g.addEdge("C", "D", 6)
g.addEdge("D", "B", 8)
g.addEdge("D", "C", 6)
g.addEdge("E", "A", 15)
g.addEdge("E", "C", 20)

g.kruskalAlgo()

edges = [[0, 10, 20, 0, 0],
         [10, 0, 30, 5, 0],
         [20, 30, 0, 15, 6],
         [0, 5, 15, 0, 8],
         [0, 0, 6, 8, 0]]

nodes = ["A","B","C","D","E"]
g = Graph(5, edges, nodes)
g.primsAlgo()

