package com.example.lee.thirdRound;

import java.util.ArrayList;
import java.util.Collections;
import java.util.List;

public class PascalTriangleII {
    public List<Integer> getRow(int rowIndex) {
        if (rowIndex < 1) {
            return Collections.emptyList();
        }
        List<Integer> res = new ArrayList<>();
        res.add(1);
        for (int i = 1; i <= rowIndex; i++) {
            List<Integer> newList = new ArrayList<>();
            newList.add(1);
            for (int j = 0; j < res.size() - 1; j++) {
                newList.add(res.get(j) + res.get(j + 1));
            }
            newList.add(1);
            res = newList;
        }
        return res;
    }

    public static void main(String[] args) {
        PascalTriangleII pascalTriangleII = new PascalTriangleII();
        pascalTriangleII.getRow(3).stream().forEach(System.out::println);
    }
}
