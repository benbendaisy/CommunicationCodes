package com.example.lee.firstRound;

/**
 * Created by benbendaisy on 3/9/15.
 *
 * Write a function that takes an unsigned integer and returns the number of ’1' bits it has (also known as the Hamming weight).
 *
 * For example, the 32-bit integer ’11' has binary representation 00000000000000000000000000001011, so the function should return 3.
 */
public class Numberof1Bits {
    public int hammingWeight(int n) {
        int count = 0;
        int intSize = Integer.SIZE;
        for (int i = 0; i < intSize; i++) {
            int t = n & 1;
            if (t == 1) {
                count++;
            }
            n >>= 1;
        }
        return count;
    }

    public int hammingWeightI(int n) {
        int count = 0;
        int intSize = Integer.SIZE;
        for (int i = 0; i < intSize; i++) {
            int t = (n >> i) & 1;
            if (t == 1) {
                count++;
            }
        }
        return count;
    }
}
