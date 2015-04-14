package com.example.lee.secondRound;

import java.util.ArrayList;
import java.util.List;

/**
 * Created by benbendaisy on 4/8/15.
 * Given numRows, generate the first numRows of Pascal's triangle.
 *
 * For example, given numRows = 5,
 * Return
 *
 * [
 * [1],
 * [1,1],
 * [1,2,1],
 * [1,3,3,1],
 * [1,4,6,4,1]
 * ]
 */
public class PascalsTriangle {
    public List<List<Integer>> generate(int numRows) {
        List<List<Integer>> lli = new ArrayList<List<Integer>>();
        if (numRows < 1) return lli;
        List<Integer> list = new ArrayList<Integer>();
        list.add(1);
        lli.add(list);
        if (numRows == 1) return lli;
        list = new ArrayList<Integer>();
        list.add(1);
        list.add(1);
        lli.add(list);
        if (numRows == 2) return lli;
        numRows -= 2;
        while (numRows > 0) {
            List<Integer> lastList = lli.get(lli.size() - 1);
            list = new ArrayList<Integer>();
            list.add(1);
            for (int i = 1; i < lastList.size(); i++) {
                list.add(lastList.get(i - 1) + lastList.get(i));
            }
            list.add(1);
            lli.add(list);
            numRows--;
        }
        return lli;
    }
}
