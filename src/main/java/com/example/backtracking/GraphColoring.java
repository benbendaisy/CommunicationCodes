package com.example.backtracking;

/**
 * Created by benbendaisy on 5/22/15.
 */
public class GraphColoring {
    boolean isSafe(int v, boolean[][] graph, int color[], int c) {
        for (int i = 0; i < graph.length; i++) {
            if (graph[v][i] && c == color[i]) return false;
        }
        return true;
    }

    boolean graphColoring(boolean[][] graph, int m, int[] color, int v) {
        if (v == graph.length) return true;
        for (int c = 1; c <= m; c++) {
            if (isSafe(v, graph, color, c)) {
                color[v] = c;
                if (graphColoring(graph, m, color, v + 1)) return true;
                color[v] = 0;
            }
        }
        return false;
    }
}
