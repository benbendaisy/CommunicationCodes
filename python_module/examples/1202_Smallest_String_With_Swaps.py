from collections import defaultdict
from typing import List


class Solution:

    def smallestStringWithSwaps(self, s: str, pairs: List[List[int]]) -> str:
        length = len(s)
        visited = [False] * length
        # neighbor graph
        # forest representation by graphs
        graph = defaultdict(lambda: [])

        # converted swapped pairs to a forest represented by a graph hashmap
        # all nodes in a connected graph can be swapped each other
        for a,b in pairs:
            graph[a].append(b)
            graph[b].append(a)

        def dfsTraverse(index: int, vertexes: list, indexes: list):
            """
            traverse all connected nodes in a graph
            :param index:
            :param vertexes:
            :param indexes:
            :return:
            """
            if visited[index]:
                return
            vertexes.append(s[index])
            indexes.append(index)
            visited[index] = True
            for idx in graph[index]:
                if not visited[idx]:
                    dfsTraverse(idx, vertexes, indexes)

        answers = [""] * length

        # traverse all graphes in the forest
        for idx in range(length):
            # check if there is any graph not visited
            if not visited[idx]:
                vertexes = []
                indexes = []
                dfsTraverse(idx, vertexes, indexes)
                vertexes.sort()
                indexes.sort()
                for i in range(len(indexes)):
                    answers[indexes[i]] = vertexes[i]

        return "".join(answers)
