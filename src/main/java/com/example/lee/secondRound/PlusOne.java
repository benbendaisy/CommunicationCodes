package com.example.lee.secondRound;

import java.util.ArrayList;
import java.util.List;

/**
 * Created by benbendaisy on 5/16/15.
 */
public class PlusOne {
    public int[] plusOne(int[] digits) {
        List<Integer> list = new ArrayList<Integer>();
        if (null == digits) return new int[0];
        int crr = 1;
        for (int i = digits.length - 1; i >= 0; i--) {
            int sum = digits[i] + crr;
            list.add(0, sum % 10);
            crr = sum / 10;
        }
        if (crr != 0) list.add(0, crr);

        int[] arr = new int[list.size()];
        for (int i = 0; i < list.size(); i++) {
            arr[i] = list.get(i);
        }
        return arr;
    }
}
