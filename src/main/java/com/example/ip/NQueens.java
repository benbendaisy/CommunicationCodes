package com.example.ip;

import java.io.BufferedWriter;
import java.io.FileWriter;
import java.io.IOException;
import java.util.HashSet;
import java.util.Scanner;
import java.util.Set;

/**
 * Created by benbendaisy on 4/28/15.
 */
public class NQueens {
    static int maxThreats(int[] a) {
        if (null == a || a.length == 0) return 0;
        int max = 0;
        for (int i = 0; i < a.length; i++) {
            int lMax = queenAtackCount(i, a, a[i]);
            max = Math.max(max, lMax);
        }
        return max;
    }

    private static int queenAtackCount(int row, int[] columns, int column){
        int cnt = 0;
        Set<Double> set = new HashSet<Double>();
        for(int i = 0; i < columns.length; i++){
            if(i != row){
                double klope = (double)(columns[i] - column) / (row - i);
                if (!set.contains(columns[i]) && (Math.abs(row - i) == Math.abs(columns[i] - column) || column == columns[i])) {
                    cnt++;
                    set.add(klope);
                }
            }

        }
        return cnt;
    }

    public static void main(String[] args) {
//        int[] a = {4, 5, 1, 3, 7, 8, 2, 6};
//        System.out.println(maxThreats(a));
        Scanner in = new Scanner(System.in);
        final String fileName = System.getenv("OUTPUT_PATH");
        BufferedWriter bw = null;
        try {
            bw = new BufferedWriter(new FileWriter(fileName));
            int res = 1;

            int _a_size = Integer.parseInt(in.nextLine());
            int[] _a = new int[_a_size];
            int _a_item;
            for(int _a_i = 0; _a_i < _a_size; _a_i++) {
                _a_item = Integer.parseInt(in.nextLine());
                _a[_a_i] = _a_item;
            }

            res = maxThreats(_a);
            bw.write(String.valueOf(res));
            bw.newLine();
        } catch (IOException e) {
            e.printStackTrace();
        } finally {
            if (null != bw) {
                try {
                    bw.close();
                } catch (IOException e) {
                    e.printStackTrace();
                }
            }
        }
    }


    private static int queenAtackCountI(int row, int[] columns, int column){
        int cnt = 0;
        Set<Integer> set = new HashSet<Integer>();
        for(int i = 0; i < row; i++){
            if(column == columns[i] || Math.abs(row - i) == Math.abs(columns[i] - column)){
                cnt++;
            }
        }
        return cnt;
    }

}
