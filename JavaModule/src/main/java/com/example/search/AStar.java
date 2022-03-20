package com.example.search;

import java.awt.*;
import java.util.*;
import java.util.List;

/**
 * Created by benbendaisy on 6/7/15.
 *
 * refer to http://www.redblobgames.com/pathfinding/a-star/introduction.html?utm_source=hackernewsletter&utm_medium=email&utm_term=learn
 *
 * basic idea is using Dijkstra by Historic score
 */
public class AStar {
    private int heristic(GraphNode a, GraphNode b) {
        return Math.abs(a.point.x - b.point.x) + Math.abs(a.point.y - b.point.y);
    }

    public List<GraphNode> search(GraphNode start, GraphNode end) {
        Queue<GraphNode> frontior = new PriorityQueue<>();
        frontior.add(start);
        Map<GraphNode, GraphNode> comeFrom = new HashMap<>();
        Map<GraphNode, Integer> costSoFar = new HashMap<>();
        //comeFrom.put(start, null);
        //costSoFar.put(start, 0);
        while (!frontior.isEmpty()) {
            GraphNode current = frontior.poll();
            if (current == end) {
                List<GraphNode> list = new ArrayList<>();
                GraphNode t = current;
                while (t != start) {
                    list.add(t);
                    t = comeFrom.get(t);
                }
                list.add(start);
                Collections.reverse(list);
                return list;
            }
            for (GraphNode next : current.neighbors.keySet()) {
                int newCost = costSoFar.containsKey(current) ? costSoFar.get(current) : 0 + current.neighbors.get(next);
                if (!comeFrom.containsKey(next) || newCost < costSoFar.get(next)) {
                    costSoFar.put(next, newCost);
                    next.weight = newCost + heristic(current, next);
                    frontior.add(next);
                    comeFrom.put(next, current);
                }
            }
        }
        return new ArrayList<>();
    }

    public static void main(String[] args) {
        AStar star = new AStar();
        GraphNode node = new GraphNode(new Point(0, 0));
        GraphNode node1 = new GraphNode(new Point(1, 1));
        GraphNode node2 = new GraphNode(new Point(2, 2));
        node.neighbors.put(node1, 2);
        node.neighbors.put(node2, 3);
        GraphNode node3 = new GraphNode(new Point(3, 3));
        node1.neighbors.put(node3, 2);
        node2.neighbors.put(node3, 2);
        for (GraphNode nd : star.search(node, node3)) {
            System.out.println(nd.point.x + "," + nd.point.y);
        }
     }
}
