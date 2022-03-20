package com.example.lee.thirdRound;

public class GasStation {
    public int canCompleteCircuit(int[] gas, int[] cost) {
        if (gas == null || cost == null || gas.length != cost.length) {
            return -1;
        }
        int totalGas = 0, totalCost = 0;
        int stardIdx = 0, currentGas = 0;
        for (int i = 0; i < gas.length; i++) {
            if (currentGas < 0) {
                stardIdx = i;
                currentGas = 0;
            }
            currentGas += gas[i] - cost[i];
            totalGas += gas[i];
            totalCost += cost[i];
        }
        return totalGas >= totalCost ? stardIdx : -1;
    }
}
