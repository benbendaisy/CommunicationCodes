package com.example.lee.secondRound;

import java.util.ArrayList;
import java.util.List;

/**
 * Created by benbendaisy on 4/8/15.
 *
 * Given an index k, return the kth row of the Pascal's triangle.
 *
 * For example, given k = 3,
 * Return [1,3,3,1].
 */
public class PascalsTriangleII {
    public List<Integer> getRow(int rowIndex) {
        List<Integer> list = new ArrayList<Integer>();
        if (rowIndex < 0) return list;
        list.add(1);
        if (rowIndex == 0) return list;
        list.add(1);
        if (rowIndex == 1) return list;
        for (int i = 0; i <= rowIndex - 2; i++) {
            for (int j = list.size() - 1; j > 0; j--) {
                list.set(j, list.get(j) + list.get(j - 1));
            }
            list.add(1);
        }
        return list;
    }
}
