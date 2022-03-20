package com.example.lee.secondRound;

/**
 * Created by benbendaisy on 4/5/15.
 */
public class GasStation {
    public int canCompleteCircuit(int[] gas, int[] cost) {
        if (null == gas || null == cost || gas.length != cost.length) return -1;
        int start = -1, loc = 0, total = 0;
        for (int i = 0; i < gas.length; i++) {
            loc += gas[i] - cost[i];
            total += gas[i] - cost[i];
            if (loc < 0) {
                loc = 0;
                start = i;
            }
        }
        return total >= 0 ? start + 1 : -1;
    }
}
