package com.example.ip.zenefits;

import java.util.ArrayList;
import java.util.LinkedList;
import java.util.List;
import java.util.Queue;

/**
 * Created by benbendaisy on 6/6/15.
 *
 * 给一个graph， 找出中心点，也就是到其他所有点距离之和最小的那个点
 *
 *
 */
public class CentrilizeGraphNode {
    List<CentrilizeGraphNode> neighbors = new ArrayList<>();

    /*
     *   assume no cycles
     *   calculate node's centrilize score
     *
     */
    private int calculate(CentrilizeGraphNode node) {
        Queue<CentrilizeGraphNode> queue1 = new LinkedList<>();
        Queue<CentrilizeGraphNode> queue2 = new LinkedList<>();
        queue1.add(node);
        int level = 1, res = 0;
        while (!queue1.isEmpty()) {
            CentrilizeGraphNode nd = queue1.poll();
            for (CentrilizeGraphNode n : nd.neighbors) {
                queue2.add(n);
                res += level;
            }
            if (queue1.isEmpty()) {
                queue1 = queue2;
                queue2 = new LinkedList<>();
                level++;
            }
        }
        return res;
    }

    /*
     *   naive solution is to calculate all node's centralize score and find the least one
     *
     *   interviewer wants the solution is to make use of the relations of nodes
     *         4
     *         |
     *   1  -  2  -  3  -  5
     *
     *   for example: if graph is shown above, then the solution should be caculating any nodes have
     *   one neighbor
     *
     *   1, 4, 5 by calculate method, then 3 and 2
     *
     *   c5 - c3 = n - 1; n is then number of nodes
     *
     *   c2 = c1 + c4 + c3 - 3 * (n - 1) //not sure about this equation, which should look like this
     */


}
