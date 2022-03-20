package com.example.lee.firstRound;

/**
 * Created by benbendaisy on 12/23/14.
 * There are N gas stations along a circular route, where the amount of gas at station i is gas[i].
 * You have a car with an unlimited gas tank and it costs cost[i] of gas to travel from station i to its next station (i+1). You begin the journey with an empty tank at one of the gas stations.
 * Return the starting gas station's index if you can travel around the circuit once, otherwise return -1.
 * Note:
 * The solution is guaranteed to be unique.
 */
public class GasStation {
    public int canCompleteCircuit(int[] gas, int[] cost) {
        if(gas == null || cost == null || gas.length == 0 || cost.length == 0 || gas.length != cost.length){
            return -1;
        }
        int total = 0; //check if there is a solution
        int sum = 0; //check if current start point validate
        int startIndex = -1; // point the point just before a valid start
        int len = gas.length;
        for(int i = 0; i < len; i++){
            int remaining = gas[i] - cost[i];
            sum += remaining;
            total += remaining;
            if(sum < 0){
                startIndex = i;
                sum = 0;
            }
        }

        return total >= 0 ? startIndex + 1 : -1;
    }
}
