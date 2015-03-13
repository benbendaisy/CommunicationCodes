package com.example.lee.firstRound;

import com.example.lee.model.UndirectedGraphNode;

import java.util.*;

/**
 * Created by pzhong1 on 12/23/14.
 * Clone an undirected graph. Each node in the graph contains a label and a list of its neighbors.
 * OJ's undirected graph serialization:
 * Nodes are labeled uniquely.
 * We use # as a separator for each node, and , as a separator for node label and each neighbor of the node.
 * As an example, consider the serialized graph {0,1,2#1,2#2,2}.
 * The graph has a total of three nodes, and therefore contains three parts as separated by #.
 * First node is labeled as 0. Connect node 0 to both nodes 1 and 2.
 * Second node is labeled as 1. Connect node 1 to node 2.
 * Third node is labeled as 2. Connect node 2 to node 2 (itself), thus forming a self-cycle.
 * Visually, the graph looks like the following:
 * 1
 * / \
 * /   \
 * 0 --- 2
 * / \
 * \_/
 */

//notice: use map to keep tracking of current node and copied node
public class CloneGraph {

    //recursively copy nodes
    public UndirectedGraphNode cloneGraph(UndirectedGraphNode node) {
        if(node == null){
            return null;
        }
        Map<UndirectedGraphNode, UndirectedGraphNode> map = new HashMap<UndirectedGraphNode, UndirectedGraphNode>();
        UndirectedGraphNode head = cloneGraphHelper(node, map);
        return head;
    }

    private UndirectedGraphNode cloneGraphHelper(UndirectedGraphNode node, Map<UndirectedGraphNode, UndirectedGraphNode> map) {
        if(map.containsKey(node)){
            return map.get(node);
        }
        UndirectedGraphNode head = new UndirectedGraphNode(node.label);
        map.put(node, head);
        for(UndirectedGraphNode n : node.neighbors){
            UndirectedGraphNode currNode;
            if(map.containsKey(n)){
                currNode = map.get(n);
            } else {
                currNode = cloneGraphHelper(n, map);
            }
            head.neighbors.add(currNode);
        }
        return head;
    }

    //iteratively copy nodes
    public UndirectedGraphNode cloneGraphI(UndirectedGraphNode node) {
        if(node == null){
            return null;
        }
        Map<UndirectedGraphNode, UndirectedGraphNode> map = new HashMap<UndirectedGraphNode, UndirectedGraphNode>();
        Queue<UndirectedGraphNode> queue = new LinkedList<UndirectedGraphNode>();
        queue.add(node);
        UndirectedGraphNode head = new UndirectedGraphNode(node.label);
        map.put(node, head);
        while(!queue.isEmpty()){
            UndirectedGraphNode node1 = queue.poll();
            UndirectedGraphNode currNode;
            if(map.containsKey(node1)){
                currNode = map.get(node1);
            } else {
                currNode = new UndirectedGraphNode(node1.label);
                map.put(node1, currNode);
            }
            for(UndirectedGraphNode node1Neighbor : node1.neighbors){
                UndirectedGraphNode newNode;
                if(map.containsKey(node1Neighbor)){
                    newNode = map.get(node1Neighbor);
                } else {
                    newNode = new UndirectedGraphNode(node1Neighbor.label);
                    map.put(node1Neighbor, newNode);
                    queue.add(node1Neighbor);
                }
                currNode.neighbors.add(newNode);
            }
        }
        return head;
    }
}
