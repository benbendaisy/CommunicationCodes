package com.example.lee.model;

import java.util.ArrayList;
import java.util.List;

/**
 * Created by benbendaisy on 12/23/14.
 */
public class UndirectedGraphNode {
    int label;
    List<UndirectedGraphNode> neighbors;
    UndirectedGraphNode(int x) { label = x; neighbors = new ArrayList<UndirectedGraphNode>(); }
}
