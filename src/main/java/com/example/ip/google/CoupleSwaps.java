package com.example.ip.google;

import java.util.Arrays;
import java.util.HashMap;
import java.util.Map;

/**
 * Created by benbendaisy on 6/16/15.
 */
public class CoupleSwaps {
//    private static Integer minSwaps = null;
//    public static int minimalCoupleSwaps(int[] arr) {
//        if (null == arr || arr.length < 1) return 0;
//        minimalCoupleSwaps(arr, 0);
//        return minSwaps == null ? -1 : minSwaps;
//    }
//
//    private static void minimalCoupleSwaps(int[] arr, int idx) {
//        if (idx == arr.length) {
//            int[] newArry = Arrays.copyOf(arr, arr.length);
//            int min = coupleSort(newArry);
//            minSwaps = minSwaps == null ? min : Math.min(minSwaps, min);
//            return;
//        }
//        for (int i = idx; i < arr.length; i++) {
//            swap(arr, i, idx);
//            minimalCoupleSwaps(arr, idx + 1);
//            swap(arr, i, idx);
//        }
//    }

    public static int minimalCoupleSwaps(int[] arr) {
        if (null == arr || arr.length < 1) return 0;
        int min = Integer.MAX_VALUE;
        for (int i = 0; i < arr.length; i++) {
            for (int j = i + 1; j < arr.length; j++) {
                swap(arr, i, j);
                int[] newArry = Arrays.copyOf(arr, arr.length);
                min = Math.min(min, coupleSort(newArry) + 1);
                swap(arr, i, j);
            }
        }
        return min;
    }
    private static int coupleSort(int[] arr) {
        if (null == arr || arr.length < 1) return 0;
        int numSwap = 0;
        Map<Integer, Integer> map = new HashMap<>();
        for (int i = 0; i < arr.length; i++) {
            if (!map.containsKey(arr[i])) {
                map.put(arr[i], i);
            } else {
                if (i % 2 == 1 && map.get(arr[i]) == i - 1) continue;
                if (map.get(arr[i]) % 2 == 0) {
                    swap(arr, i, map.get(arr[i]) + 1);
                } else {
                    swap(arr, i, map.get(arr[i]) - 1);
                }
                numSwap++;
                map.remove(arr[i]);
                i--;
            }
        }
        return numSwap;
    }

    private static void swap(int[] arr, int i, int j) {
        //System.out.println("i: " + i + ", j: " + j);
        int t = arr[i];
        arr[i] = arr[j];
        arr[j] = t;
    }

    public static void main(String[] args) {
        int[] arr = {1, 2, 3, 4, 4, 3, 2, 1};
        System.out.println(minimalCoupleSwaps(arr));
        System.out.println(coupleSort(arr));
    }
}
