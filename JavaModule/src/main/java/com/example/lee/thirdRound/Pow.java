package com.example.lee.thirdRound;

import java.util.HashMap;
import java.util.Map;

/**
 * Created by benbendaisy on 7/8/17.
 */
public class Pow {
    public double myPow(double x, int n) {
        double res;
        Map<Long, Double> cachedMap = new HashMap<>();
        if (n > 0) {
            res = myPowHelper(x, n, cachedMap);
        } else {
            res = 1 / myPowHelper(x, Math.abs((long) n), cachedMap);
        }
        return res;
    }
    private double myPowHelper(double x, long n, Map<Long, Double> cachedMap) {
        if (n == 0) {
            return 1.0;
        }
        if (cachedMap.containsKey(n)) {
            return cachedMap.get(n);
        }
        double res = myPowHelper(x, n/2, cachedMap);
        res = res * res;
        if (n % 2 != 0) {
            res = res * x;
        }
        cachedMap.put(n, res);
        return res;
    }

    public static void main(String[] args) {
        Pow pow = new Pow();
        System.out.println(pow.myPow(2.0, -2147483648));
    }
}
