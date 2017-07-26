package com.example.lee.thirdRound;

import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;

public class GrayCode {
    public List<Integer> grayCode(int n) {
        if (n == 0) {
            return Arrays.asList(0);
        }
        List<Integer> list = grayCode(n - 1);
        List<Integer> newList = new ArrayList<>();
        newList.addAll(list);
        int adding = 1 << n - 1;
        for (int i = list.size() - 1; i >= 0; i--) {
            newList.add(list.get(i) + adding);
        }
        return newList;
    }
}
