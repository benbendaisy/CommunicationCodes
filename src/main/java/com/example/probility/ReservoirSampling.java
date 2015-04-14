package com.example.probility;

import java.util.Random;

/**
 * Created by benbendaisy on 3/17/15.
 *
 * (k/(i-1)) * ((i-1)/i)=k/i. i is the length of input array
 */
public class ReservoirSampling {
    public int[] selectKSamples(int[] data, int k) {
        if (null == data || data.length <= k) return data;
        int[] pool = new int[k];
        for (int i = 0; i < k; i++) {
            pool[i] = data[i];
        }
        for (int i = k; i < data.length; i++) {
            Random random = new Random();
            //int rand = (int) (Math.random() * (i + 1));
            int rand = random.nextInt(i + 1);
            if (rand < k) {
                pool[rand] = data[i];
            }
        }
        return pool;
    }

    private void printArray(int[] A) {
        for (int num : A) System.out.print(num + " ");
        System.out.println("");
    }

    public static void main(String[] args) {
        ReservoirSampling reservoirSampling = new ReservoirSampling();
        int[] data = {1, 2, 3, 4, 5, 6};
        reservoirSampling.printArray(reservoirSampling.selectKSamples(data, 3));
    }
}
