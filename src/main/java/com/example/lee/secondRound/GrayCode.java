package com.example.lee.secondRound;

import java.util.ArrayList;
import java.util.List;

/**
 * Created by benbendaisy on 5/1/15.
 *
 * The gray code is a binary numeral system where two successive values differ in only one bit.
 *
 * Given a non-negative integer n representing the total number of bits in the code, print the sequence of gray code. A gray code sequence must begin with 0.
 *
 * For example, given n = 2, return [0,1,3,2]. Its gray code sequence is:
 *
 * 00 - 0
 * 01 - 1
 * 11 - 3
 * 10 - 2
 */
public class GrayCode {
    public List<Integer> grayCode(int n) {
        List<Integer> list = new ArrayList<Integer>();
        if (n == 0) {
            list.add(0);
            return list;
        }
        List<Integer> newList = grayCode(n - 1);
        list.addAll(newList);
        int adding = 1 << n - 1;
        for (int i = newList.size() - 1; i >= 0; i--) {
            int e = newList.get(i) + adding;
            list.add(e);
        }
        return list;
    }

    public static void main(String[] args) {
        int adding = 1 << 5;
        System.out.println(adding);
    }
}
