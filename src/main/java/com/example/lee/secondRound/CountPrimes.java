package com.example.lee.secondRound;

import java.util.Arrays;

/**
 * Created by benbendaisy on 4/28/15.
 *
 * Count the number of prime numbers less than a non-negative number, n
 */
public class CountPrimes {
    public int countPrimes(int n) {
        long start = System.currentTimeMillis();
        if (n < 3) return 0;
        boolean[] primes = new boolean[n];
        Arrays.fill(primes, true);
        primes[0] = false;
        primes[1] = false;
        for (int i = 2; i < n; i++) {
            if (primes[i]) {
                for(int j = 2; j * i < n; j++) {
                    primes[i * j] = false;
                }
            }
        }
        int cnt = 0;
        for (int i = 1; i < n; i++) {
            if (primes[i]) cnt++;
        }
        long end = System.currentTimeMillis();
        System.out.println("c1: " + (end - start));
        return cnt;
    }

    //both pass large tests
    public int countPrimesI(int n) {
        long start = System.currentTimeMillis();
        if (n < 3) return 0;
        int cnt = 1;
        for (int i = 3; i < n; i++) {
            if (isPrime(i)) cnt++;
        }
        long end = System.currentTimeMillis();
        System.out.println("c2: " + (end - start));
        return cnt;
    }
    private boolean isPrime(int m) {
        if (m % 2 == 0) return false;
        for (int i = 3; i * i <= m; i += 2) {
            if (m % i == 0) return false;
        }
        return true;
    }

    public static void main(String[] args) {
        CountPrimes countPrimes = new CountPrimes();
        System.out.println(countPrimes.countPrimes(1500000));
        System.out.println(countPrimes.countPrimesI(1500000));
    }
}
