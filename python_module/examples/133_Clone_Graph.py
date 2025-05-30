"""
# Definition for a Node.
"""
from collections import deque


class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []


class Solution:
    """
        Given a reference of a node in a connected undirected graph.

        Return a deep copy (clone) of the graph.

        Each node in the graph contains a value (int) and a list (List[Node]) of its neighbors.

        class Node {
            public int val;
            public List<Node> neighbors;
        }

        Test case format:

        For simplicity, each node's value is the same as the node's index (1-indexed). For example, the first node with val == 1, the second node with val == 2, and so on. The graph is represented in the test case using an adjacency list.

        An adjacency list is a collection of unordered lists used to represent a finite graph. Each list describes the set of neighbors of a node in the graph.

        The given node will always be the first node with val = 1. You must return the copy of the given node as a reference to the cloned graph.

        Example 1:

        Input: adjList = [[2,4],[1,3],[2,4],[1,3]]
        Output: [[2,4],[1,3],[2,4],[1,3]]
        Explanation: There are 4 nodes in the graph.
        1st node (val = 1)'s neighbors are 2nd node (val = 2) and 4th node (val = 4).
        2nd node (val = 2)'s neighbors are 1st node (val = 1) and 3rd node (val = 3).
        3rd node (val = 3)'s neighbors are 2nd node (val = 2) and 4th node (val = 4).
        4th node (val = 4)'s neighbors are 1st node (val = 1) and 3rd node (val = 3).
        Example 2:


        Input: adjList = [[]]
        Output: [[]]
        Explanation: Note that the input contains one empty list. The graph consists of only one node with val = 1 and it does not have any neighbors.
        Example 3:

        Input: adjList = []
        Output: []
        Explanation: This an empty graph, it does not have any nodes.
    """
    def cloneGraph1(self, node: 'Node') -> 'Node':
        if not node:
            return node
        que, clone = deque([node]), {node.val: Node(node.val, [])}
        while que:
            cur_node = que.popleft()
            cur_clone = clone[cur_node.val]

            for neighbor in cur_node.neighbors:
                if neighbor.val not in clone:
                    clone[neighbor.val] = Node(neighbor.val, [])
                    que.append(neighbor)
                cur_clone.neighbors.append(clone[neighbor.val])
        return clone[node.val]
    
    def cloneGraph(self, node: 'Node') -> 'Node':
        if not node:
            return node
        graph, que = {node: Node(node.val, [])}, deque([node])
        while que:
            cur_node = que.popleft()
            for neighbor in cur_node.neighbors:
                if neighbor not in graph:
                    graph[neighbor] = Node(neighbor.val, [])
                    que.append(neighbor)
                graph[cur_node].neighbors.append(graph[neighbor])
        return graph[node]