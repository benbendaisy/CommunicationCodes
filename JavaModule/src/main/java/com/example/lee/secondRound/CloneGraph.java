package com.example.lee.secondRound;

import com.example.lee.model.UndirectedGraphNode;

import java.util.HashMap;
import java.util.LinkedList;
import java.util.Map;
import java.util.Queue;

/**
 * Created by benbendaisy on 4/5/15.
 */
public class CloneGraph {

    // clone graph by dfs
    public UndirectedGraphNode cloneGraph(UndirectedGraphNode node) {
        if (null == node) return node;
        Map<Integer, UndirectedGraphNode> visited = new HashMap<Integer, UndirectedGraphNode>();
        return cloneGraph(node, visited);
    }

    public UndirectedGraphNode cloneGraph(UndirectedGraphNode node, Map<Integer, UndirectedGraphNode> visited) {
        UndirectedGraphNode root = new UndirectedGraphNode(node.label);
        visited.put(node.label, root);
        for (UndirectedGraphNode u : node.neighbors) {
            UndirectedGraphNode nu = null;
            if (visited.containsKey(u.label)) {
                nu = visited.get(u.label);
            } else {
                nu = cloneGraph(u, visited);
            }
            root.neighbors.add(nu);
        }
        return root;
    }

    //clone graph by bfs
    public UndirectedGraphNode cloneGraphI(UndirectedGraphNode node) {
        if (null == node) return node;
        Map<Integer, UndirectedGraphNode> visited = new HashMap<Integer, UndirectedGraphNode>();
        Queue<UndirectedGraphNode> que = new LinkedList<UndirectedGraphNode>();
        que.add(node);
        while (!que.isEmpty()) {
            UndirectedGraphNode u = que.poll();
            UndirectedGraphNode nu = null;
            if (visited.containsKey(u.label)) {
                nu = visited.get(u.label);
            } else {
                nu = new UndirectedGraphNode(u.label);
                visited.put(u.label, nu);
            }
            for (UndirectedGraphNode l : u.neighbors) {
                UndirectedGraphNode nl = null;
                if (visited.containsKey(l.label)) {
                    nl = visited.get(l.label);
                } else {
                    nl = new UndirectedGraphNode(l.label);
                    visited.put(l.label, nl);
                    que.add(l);
                }
                nu.neighbors.add(nl);
            }
        }
        return visited.get(node.label);
    }

    public static void main(String[] args) {
        Queue<UndirectedGraphNode> que = new LinkedList<UndirectedGraphNode>();
        que.poll();
    }

}
