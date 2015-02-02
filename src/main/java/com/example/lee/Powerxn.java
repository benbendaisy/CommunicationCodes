package com.example.lee;

import java.util.HashMap;
import java.util.Map;

/**
 * Created by benbendaisy on 1/27/15.
 *
 * Implement pow(x, n).
 */
public class Powerxn {
    public double pow(double x, int n) {
        Map<Long, Double> map = new HashMap<Long, Double>();
        if(n < 0){
            long m = -1 * ((long) n);
            return 1 / powHelper(x, m, map);
        } else {
            return powHelper(x, n, map);
        }
    }

    public double powHelper(double x, long n, Map<Long, Double> map){
        if(n == 0){
            return 1;
        } else if(n == 1){
            return x;
        } else if(map.containsKey(n)){
            return map.get(n);
        }

        long mid = n / 2;

        double result = powHelper(x, mid, map) * powHelper(x, n - mid, map);
        map.put(n, result);
        return result;
    }
}
