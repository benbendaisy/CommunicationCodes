package com.example.backtracking;

import java.util.Arrays;

/**
 * Created by benbendaisy on 5/22/15.
 */
public class HamiltonianCycle {
    private boolean isSafe(int v, boolean[][] graph, int path[], int pos) {
        if (!graph[path[pos - 1]][v]) return false;
        for (int i = 0; i < pos; i++) {
            if (path[i] == v) return false;
        }
        return true;
    }

    private boolean hasCycleUtil(boolean[][] graph, int[] path, int pos) {
        if (pos == graph.length) {
            return graph[path[pos - 1]][path[0]] ? true : false;
        }
        for (int v = 1; v < graph.length; v++) {
            if (isSafe(v, graph, path, pos)) {
                path[pos] = v;
                if (hasCycleUtil(graph, path, pos + 1)) return true;
                path[pos] = -1;
            }
        }
        return false;
    }

    public boolean hasCycleUtil(boolean[][] graph) {
        int[] path = new int[graph.length];
        Arrays.fill(path, -1);
        path[0] = 0;
        if (hasCycleUtil(graph, path, 1)){
            for (int v : path) {
                System.out.println(v);
            }
            System.out.println(path[0]);
            return true;
        }
        System.out.println("no cycles.");
        return false;
    }

    public static void main(String[] args) {
        HamiltonianCycle hamiltonianCycle = new HamiltonianCycle();
        boolean[][] graph1 = {{false, true, false, true, false},
            {true, false, true, true, true},
            {false, true, false, false, true},
            {true, true, false, false, true},
            {false, true, true, true, false},
        };
        hamiltonianCycle.hasCycleUtil(graph1);
    }

}
