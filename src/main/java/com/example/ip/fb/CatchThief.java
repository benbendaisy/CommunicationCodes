package com.example.ip.fb;

import java.util.Arrays;

/**
 * Created by benbendaisy on 6/2/15.
 */
public class CatchThief {
    public boolean alibaba(int numCaves, int[] strategy) {
        if (numCaves < 1 || null == strategy || strategy.length == 0) return false;
        int len = strategy.length;
        boolean[] survial = new boolean[numCaves + 2];
        Arrays.fill(survial, true);
        survial[0] = false;
        survial[numCaves + 1] = false;
        survial[strategy[0]] = false;
        for (int i = 1; i < len; i++) {
            for (int j = 1; j <= numCaves; j++) {
                survial[j] = ((survial[j - 1] || survial[j + 1]) && strategy[i] != j - 1) ? true : false;
            }
        }

        for (int i = 1; i <= numCaves; i++) if (survial[i]) return false;
        return true;
    }

    public static void main(String[] args) {
        int[] strategy = {1, 1};
        CatchThief catchThief = new CatchThief();
        System.out.println(catchThief.alibaba(3, strategy));
    }
}
