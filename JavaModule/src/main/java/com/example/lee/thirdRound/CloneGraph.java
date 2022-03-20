package com.example.lee.thirdRound;

import com.example.lee.model.UndirectedGraphNode;

import java.util.*;

public class CloneGraph {
    public UndirectedGraphNode cloneGraph(UndirectedGraphNode node) {
        if (node == null) {
            return null;
        }
        Map<UndirectedGraphNode, UndirectedGraphNode> visited = new HashMap<>();
        return cloneGraphHelper(node, visited);
    }

    private UndirectedGraphNode cloneGraphHelper
            (UndirectedGraphNode node, Map<UndirectedGraphNode, UndirectedGraphNode> visited) {
        if (visited.containsKey(node)) {
            return visited.get(node);
        }
        UndirectedGraphNode newNode = new UndirectedGraphNode(node.label);
        visited.put(node, newNode);
        for (UndirectedGraphNode nd : node.neighbors) {
            UndirectedGraphNode newNd = cloneGraphHelper(nd, visited);
            newNode.neighbors.add(newNd);
        }
        return newNode;
    }
}
