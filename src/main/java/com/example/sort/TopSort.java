package com.example.sort;

import java.util.*;

/**
 * Created by benbendaisy on 3/11/15.
 */
public class TopSort {
    private static void toposort(List<List<Integer>> graph, int[] indegs) {
        int n = indegs.length;
        boolean[] visited = new boolean[n];
        Queue<Integer> queue = new PriorityQueue<Integer>();
        List<Integer> res = new ArrayList<Integer>();
        //initialize nodes with zero in-degrees
        for (int i = 0; i < n; i++) {
            if (indegs[i] == 0) {
                queue.add(i);
            }
        }

        while (!queue.isEmpty()) {
            int node = queue.poll();
            //assume node start from 1 but not 0
            res.add(node + 1);
            visited[node] = true;
            for (int nb : graph.get(node)) {
                if (visited[nb]) {
                    break;
                }
                indegs[nb]--;
                if (indegs[nb] == 0) {
                    queue.add(nb);
                }
            }
        }

        if (res.size() < n) {
            System.out.println("top sort is not successful!");
        } else {
            System.out.println(res);
        }
    }

    public static void main(String[] args) {
        Scanner in = new Scanner(System.in);
        int n = in.nextInt(), m = in.nextInt();

        // initial graph
        List<List<Integer>> graph = new ArrayList<List<Integer>>(n);
        int[] indegs = new int[n];
        for (int i=0; i<n; ++i) {
            graph.add(new ArrayList<Integer>(n));
        }

        // parse edges
        for (int j=0; j<m; ++j) {
            int v1 = in.nextInt() - 1, v2 = in.nextInt() - 1;
            // add v2 to v1's neighbor list
            graph.get(v1).add(v2);
            // increase v2's indegree
            indegs[v2]++;
        }

        toposort(graph, indegs);
    }
}
