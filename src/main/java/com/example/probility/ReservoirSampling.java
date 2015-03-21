package com.example.probility;

/**
 * Created by benbendaisy on 3/17/15.
 */
public class ReservoirSampling {
    public int[] selectKSamples(int[] data, int k) {
        if (null == data || data.length <= k) return data;
        int[] pool = new int[k];
        for (int i = 0; i < k; i++) {
            pool[i] = data[i];
        }
        for (int i = k; i < data.length; i++) {
            int rand = (int) (Math.random() * (i + 1));
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
