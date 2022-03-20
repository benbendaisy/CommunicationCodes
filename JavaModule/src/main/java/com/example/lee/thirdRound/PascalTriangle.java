package com.example.lee.thirdRound;

import java.util.ArrayList;
import java.util.Arrays;
import java.util.Collections;
import java.util.List;

public class PascalTriangle {
    public List<List<Integer>> generate(int numRows) {
        List<List<Integer>> res = new ArrayList<>();
        if (numRows <= 1) {
            return Collections.emptyList();
        }
        res.add(Arrays.asList(1));
        for (int i = 1; i < numRows; i++) {
            List<Integer> list = res.get(res.size() - 1);
            List<Integer> newList = new ArrayList<>();
            newList.add(1);
            for (int j = 0; j < list.size() - 1; j++) {
                newList.add(list.get(j) + list.get(j + 1));
            }
            newList.add(1);
            res.add(newList);
        }
        return res;
    }
}
