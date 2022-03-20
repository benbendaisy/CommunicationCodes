package com.example.search;

import java.awt.*;
import java.util.HashMap;
import java.util.Map;

/**
 * Created by benbendaisy on 6/7/15.
 */
public class GraphNode implements Comparable<GraphNode> {
    public Point point;
    Map<GraphNode, Integer> neighbors;
    public int weight;
    public GraphNode(Point point) {
        this.point = point;
        this.neighbors = new HashMap<>();
    }

    @Override
    public int compareTo(GraphNode other) {
        return this.weight < other.weight ? -1 : (this.weight > other.weight ? 1 : 0);
    }
}
