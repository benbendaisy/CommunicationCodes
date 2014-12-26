package com.example.lee.model;

import java.util.ArrayList;
import java.util.List;

/**
 * Created by benbendaisy on 12/23/14.
 */
public class UndirectedGraphNode {
    public int label;
    public List<UndirectedGraphNode> neighbors;
    public UndirectedGraphNode(int x) { label = x; neighbors = new ArrayList<UndirectedGraphNode>(); }
}
